import base64
import os
import random
import string

import pytz
from django.db import transaction
from django.http import JsonResponse
from PIL import Image
import io
import requests
from django.core.files.base import ContentFile
import requests
from datetime import datetime

from django.contrib.auth.hashers import check_password
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect
from drf_yasg.utils import swagger_auto_schema
from google.oauth2 import id_token as google_id_token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import UserSerializer, LoginSerializer, PostUserSerializer, GetAdminSerializer, GetUserSerializer, SellerSerializer
from rest_framework import generics, permissions
from .models import CheckEmail, UserModel
from rest_framework.decorators import api_view
from rest_framework import viewsets
import jwt
from django.conf import settings
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()  # ใช้ get_user_model() แทนการ import User โดยตรง

# Add near the top with other utility functions
def resize_image(image):
    if not image:
        return None
    try:
        img = Image.open(image)
        img.thumbnail((800, 800))  # Resize to max dimensions
        output = io.BytesIO()
        img.save(output, format='JPEG', quality=85)
        output.seek(0)
        return ContentFile(output.read(), name=image.name)
    except Exception:
        return image


# Send email
class SendEmail(APIView):
    @swagger_auto_schema(
        tags=["Email Authentication"], request_body=PostUserSerializer, responses={200: "Success"}
    )
    def post(self, request):
        user_email = request.data.get('email')
        if not user_email:
            return Response(
                {"message": "Please enter your e-mail."}, status=status.HTTP_400_BAD_REQUEST
            )

        random_code = "".join(
            random.choices(string.digits, k=6)
        )  # Generate 6-digit random string
        subject = "[tourdna.co.kr] Membership verification code"
        body = f"Email verification code: {random_code}"  # Add to random code body
        email = EmailMessage(
            subject,
            body,
            to=[user_email],
        )
        email.send()

        # Save authentication code to DB
        code = CheckEmail.objects.create(code=random_code, email=user_email)
        return Response(
            {"message": "Your email has been sent. Please check your mailbox."},
            status=status.HTTP_200_OK,
        )


class CheckEmailView(APIView):
    def post(self, request):
        # # Most recent authentication code instance
         #code_obj = (
         # CheckEmail.objects.filter(email=email).order_by("-created_at").first()
         # )
         # # Check after deployment
        code = request.data.get('code')
        email = request.data.get('email')
        code_obj = CheckEmail.objects.filter(email=email, code=code).first()
        if code_obj is None:
            return Response(
                {"message": "No verification code was sent to that email."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        tz = pytz.timezone("Asia/Vientiane")

        # If the authentication code has expired
        if code_obj.expires_at < datetime.now(tz=tz):
            code_obj.delete()
            return Response(
                {"message": "The verification code has expired."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        code_obj.delete()  # Delete email verification code
        return Response(
            {"message": "Email verification has been completed.", "is_checked": True},
            status=status.HTTP_200_OK,
        )


# Login user nad owner
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get("email")
        password = data.get("password")

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return Response(data={"message": "Email does not exist."}, status=400)

        if not check_password(password, user.password):
            return Response(data={"message": "Incorrect password."}, status=400)

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            token = serializer.validated_data
            user = UserModel.objects.get(email=data.get('email'))
            is_owner = user.is_owner
            is_admin = user.is_admin
            
            return Response(data={'token': token,
                                  "user_id": user.id,
                                  "is_admin": is_admin,
                                  "is_owner": is_owner,
                                  "user_name": user.nickname,
                                  "email": user.email if user.email else False,
                                  }, status=200)
        else:
            return Response(data={'message': 'An error occurred. Please contact the administrator.'}, status=400)

# User register
class SignupView(APIView):
    
    @swagger_auto_schema(
        tags=["join the membership"],
        request_body=PostUserSerializer,
        responses={200: "Success"},
    )
    def post(self, request):
        with transaction.atomic():
            category = request.data.get("category")
            email = request.data.get("email")
            code = request.data.get("code")
            password = request.data.get("password")
            password2 = request.data.get("password2")
            profile_image = request.data.get("profile_image")
            code_obj = CheckEmail.objects.filter(email=email, code=code).first()

            # Check whether the password and password match
            if password != password2:
                return JsonResponse(
                    {
                        "message": "Your password and password confirmation do not match."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Check for email duplicates
            user = UserModel.objects.filter(email=email)
            if user.exists():
                return Response(
                    {"message": "The email already exists."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if code_obj is None:
                return Response(
                    {"message": "No verification code was sent to that email."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            tz = pytz.timezone("Asia/Vientiane")

            # If the verification code has expired
            if code_obj.expires_at < datetime.now(tz=tz):
                code_obj.delete()
                return Response(
                    {"message": "The verification code has expired."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Check if your email matches

            if profile_image == "undefined" or profile_image is None:
                # If the image comes as an empty value, use copy to change it!
                # deepcopy -> Import copy module? -> Complete copy! (safe)
                # Consider using try, except -> Additional exception handling!
                data = request.data.copy()
                data["profile_image"] = None
                serializer = UserSerializer(data=data)
            else:
                serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                """
                Add store-specific membership registration logic
                """
                if category != "2":
                    code_obj.delete()  # Delete email verification code
                    serializer.save()
                if category == "2":
                    name = request.data.get("name")
                    address = request.data.get("address")
                    if not name or not address:
                        return Response(
                            {"message": "Please enter all required information."},
                            status.HTTP_400_BAD_REQUEST,
                        )
                    serializer.save(is_seller=True)

                return Response(
                    {"message": "Your registration has been completed."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"message": f"{serializer.errors}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

# User-related logic
class UserView(APIView):
    def get(self, request):
        user = get_object_or_404(UserModel, email=request.user)
        data = {}
        data["user_info"] = GetUserSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        <Reset password>
         Reset password if lost
        """
        email = request.data.get("email")
        password = request.data.get("password")
        password2 = request.data.get("password2")

        # Check if your email matches
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return Response(
                {"message": "Email does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if password != password2:
            return Response({'message': 'Your passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

        # Update password
        user.set_password(password)
        user.save()

        return Response({"message": "Your password has been changed."}, status=status.HTTP_200_OK)

    def patch(self, request):
        """
        <Change password>
         Change password after logging in
        """
        try:
            user = get_object_or_404(UserModel, id=request.user.id)
            origin_password = request.data.get("origin_password")
            new_password = request.data.get("password")
            check_new_password = request.data.get("password2")
            data = request.data.copy()
            image = request.data.get('profile_image')

            # When changing your password
            if (
                    new_password != check_new_password
                    or not new_password
                    or not check_new_password
            ):
                return Response(
                    {"message": "New password does not match"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Verify original password matches
            if not check_password(origin_password, user.password):
                return Response(
                    {"message": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST
                )
            if image == 'undefined' or not image:
                data['profile_image'] = None

            if not new_password:
                print(data)
                user.profile_image = data['profile_image']
                user.save()
                return Response({"message": "Modifications completed!",
                                 "image": user.profile_image.url if user.profile_image else False
                                 }, status=status.HTTP_200_OK)
            else:
                serializer = UserSerializer(user, data=data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    # If you change your password
                    return Response({"message": "Modifications completed!",
                                     "image": user.profile_image.url if user.profile_image else False
                                     }, status=status.HTTP_200_OK)
                else:
                    print(serializer.errors)
                    return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(str(e))
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=["Password change and withdrawal"], responses={200: "Success"})
    # Delete member
    def delete(self, request):
        try:
            user = request.user
            user.delete()
            return Response(
                {"message": "I deleted my account."}, status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            print(e)
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ChangeUserProfile(APIView):
    def patch(self, request):
        user = get_object_or_404(UserModel, id=request.user.id)
        image = request.data.get('profile_image')
        data = request.data.copy()

        if image == 'undefined' or not image:
            data['profile_image'] = None
        user.profile_image = resize_image(data['profile_image'])
        user.save()
        return Response({"message": "Modifications completed!",
                         "image": user.profile_image.url if user.profile_image else False
                         }, status=status.HTTP_200_OK)


class CheckToken(APIView):

    def post(self, request):
        try:
            token = request.data.get("token")
            # token decode
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            # Check expiration time
            expiration_time = decoded_token.get("exp")
            return Response({"result": "success"}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            # If the token has expired
            return Response({"result": "fail"}, status=status.HTTP_200_OK)
        except jwt.InvalidTokenError:
            # In case of invalid token
            return Response({"result": "fail"}, status=status.HTTP_200_OK)

class AdminManagementView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, id=None):
        if id:
            admin = get_object_or_404(UserModel, id=id, is_admin=True)
            serializer = GetAdminSerializer(admin)
            return Response(serializer.data)
        admins = UserModel.objects.filter(is_admin=True)
        serializer = GetAdminSerializer(admins, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            # สร้าง user ใหม่
            user = UserModel.objects.create(
                email=request.data.get('email'),
                nickname=request.data.get('nickname'),
                is_admin=True,
                is_active=True,
                is_owner=False
            )
            
            # ตั้งค่ารหัสผ่าน
            if 'password' in request.data:
                user.set_password(request.data['password'])
            
            # จัดการรูปโปรไฟล์
            if 'profile_image' in request.FILES:
                user.profile_image = request.FILES['profile_image']
            
            user.save()
            
            return Response(
                {
                    "message": "Admin created successfully",
                    "user": GetAdminSerializer(user).data
                }, 
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(f"Error creating admin: {str(e)}")  # เพิ่ม print เพื่อดู error
            return Response(
                {"message": f"Failed to create admin: {str(e)}"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, id=None):
        if not id:
            return Response(
                {"message": "ID is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        admin = get_object_or_404(UserModel, id=id, is_admin=True)
        serializer = GetAdminSerializer(admin, data=request.data, partial=True)
        
        if serializer.is_valid():
            user = serializer.save()
            if 'password' in request.data and request.data['password']:
                user.set_password(request.data['password'])
                user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        email = request.data.get('email')
        try:
            user = UserModel.objects.get(email=email)
            if user.is_owner:
                return Response(
                    {"message": "Cannot delete owner account"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # ลบ user ออกจากระบบเลย แทนที่จะแค่เปลี่ยน is_admin
            user.delete()
            
            return Response(
                {"message": f"Admin {email} has been deleted successfully"},
                status=status.HTTP_200_OK
            )
        except UserModel.DoesNotExist:
            return Response(
                {"message": "User not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, id=None):
        try:
            if id:
                user = User.objects.get(id=id, is_staff=False)
                serializer = UserSerializer(user)
            else:
                users = User.objects.filter(is_staff=False)
                serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"Error in UserListView: {str(e)}")
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, id):
        try:
            user = User.objects.get(id=id, is_staff=False)
            user.delete()
            return Response(
                {"message": "User deleted successfully"}, 
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"Error deleting user: {str(e)}")
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserManagementView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        try:
            # เปลี่ยนจาก is_staff เป็น is_admin
            users = User.objects.filter(is_admin=False)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error in UserManagementView: {str(e)}")
            return Response(
                {"error": f"Failed to fetch users: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, id):
        try:
            # เปลี่ยนจาก is_staff เป็น is_admin
            user = User.objects.get(id=id, is_admin=False)
            user.delete()
            return Response(
                {"message": "User deleted successfully"}, 
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"Error deleting user: {str(e)}")
            return Response(
                {"error": f"Failed to delete user: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
