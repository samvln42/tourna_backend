# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status, generics, filters, permissions
from django.http import Http404
from .models import Tour, Hotel, Restaurant, Packet, Guide, Ticket, Sitemain, ImagebannerModel, ImageTicketModel
from django.contrib.auth import get_user_model
from django.db import transaction
from django.contrib.auth.models import User

from .serializers import (
    TourSerializer,
    TourCreateSerializer,
    HotelSerializer,
    HotelCreateSerializer,
    RestaurantSerializer,
    RestaurantCreateSerializer,
    PacketSerializer,
    PacketCreateSerializer,
    GuideSerializer,
    GuideCreateSerializer,
    TicketSerializer,
    TicketCreateSerializer,
    SitemainSerializer, SitemainCreateSerializer,
    ImagebannerSerializer,
    UserSerializer
)


# ====================================================================================================
# Tour management's by oudone
class TourListAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description", "address"]  # เพิ่มฟิลด์ที่ต้องการค้นหา


class TourRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Tour not found"})


class TourCreateAPIView(generics.CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class TourUpdateAPIView(generics.UpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Tour not found"})


class TourDestroyAPIView(generics.DestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Tour not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)


# ====================================================================================================


# Hotel management's by oudone
class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]  # Specify fields you want to search


class HotelRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Hotel not found"})


class HotelCreateAPIView(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class HotelUpdateAPIView(generics.UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Hotel not found"})


class HotelDestroyAPIView(generics.DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Hotel not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)


# Restaurant management's by oudone
class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]  # Specify fields you want to search


class RestaurantRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Restaurant not found"})


class RestaurantCreateAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class RestaurantUpdateAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Restaurant not found"})


class RestaurantDestroyAPIView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Restaurant not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)


# Packet management's by oudone
class PacketListAPIView(generics.ListAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]  # Specify fields you want to search


class PacketRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Packet not found"})


class PacketCreateAPIView(generics.CreateAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class PacketUpdateAPIView(generics.UpdateAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Packet not found"})


class PacketDestroyAPIView(generics.DestroyAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Packet not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)


# Guide management's by oudone
class GuideListAPIView(generics.ListAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]  # Specify fields you want to search


class GuideRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Guide not found"})


class GuideCreateAPIView(generics.CreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class GuideUpdateAPIView(generics.UpdateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Guide not found"})


class GuideDestroyAPIView(generics.DestroyAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Guide not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)


# API Ticket list
class TicketListAPIView(APIView):
    def get(self, request):
        try:
            category = request.query_params.get('category', None)
            if category:
                tickets = Ticket.objects.filter(category=category)
            else:
                tickets = Ticket.objects.all()
            
            serializer = TicketSerializer(tickets, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


# API Ticket Detail
class TicketRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Ticket not found"})


# API Ticket Create
class TicketCreateAPIView(APIView):
    def post(self, request):
        try:
            with transaction.atomic():
                # สร้าง ticket
                serializer = TicketSerializer(data=request.data)
                if serializer.is_valid():
                    ticket = serializer.save()
                    
                    # จัดการรูปภาพเพิ่มเติม
                    if 'additional_images' in request.FILES:
                        for image in request.FILES.getlist('additional_images'):
                            ImageTicketModel.objects.create(
                                ticket=ticket,
                                image=image
                            )
                    
                    # ดึงข้อมูลที่อัพเดทแล้ว
                    updated_ticket = Ticket.objects.get(id=ticket.id)
                    return Response(
                        {
                            "message": "Ticket created successfully",
                            "ticket": TicketSerializer(updated_ticket).data
                        },
                        status=status.HTTP_201_CREATED
                    )
                
                print("Validation errors:", serializer.errors)
                return Response(
                    {
                        "message": "Invalid data",
                        "errors": serializer.errors
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        except Exception as e:
            print("Error creating ticket:", str(e))
            return Response(
                {
                    "message": "Failed to create ticket",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


# API Ticket Updete
class TicketUpdateAPIView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Ticket not found"})


# API Ticket Delete
class TicketDestroyAPIView(generics.DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Ticket not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)


# main page API 1
# API Sitemain list
class SitemainListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            sitemain = Sitemain.objects.last()
            sitemain_data = {}
            if sitemain:
                sitemain_data = {
                    'id': sitemain.id,
                    'logo': request.build_absolute_uri(sitemain.logo.url) if sitemain.logo else None
                }

            banners = ImagebannerModel.objects.all().order_by('-created_at')
            banner_data = []
            for banner in banners:
                if banner.image:
                    banner_data.append({
                        'id': banner.id,
                        'image': request.build_absolute_uri(banner.image.url),
                        'created_at': banner.created_at,
                        'updated_at': banner.updated_at
                    })

            response_data = {
                'sitemain': sitemain_data,
                'banners': banner_data
            }

            return Response(response_data)
            
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# API Sitemain Detail
class SitemainRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Sitemain.objects.all()
    serializer_class = SitemainSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Sitemain not found"})


# API Sitemain Create
class SitemainCreateAPIView(generics.CreateAPIView):
    queryset = Sitemain.objects.all()
    serializer_class = SitemainSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()
            
            response_data = {
                'id': instance.id,
                'message': 'success'
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


# API Sitemain Updete
class SitemainUpdateAPIView(generics.UpdateAPIView):
    queryset = Sitemain.objects.all()
    serializer_class = SitemainCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Sitemain not found"})


# API Sitemain Delete
class SitemainDestroyAPIView(generics.DestroyAPIView):
    queryset = Sitemain.objects.all()
    serializer_class = SitemainSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Sitemain not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)


# Imagebanner management's by oudone
class ImagebannerCreateAPIView(generics.CreateAPIView):
    queryset = ImagebannerModel.objects.all()
    serializer_class = ImagebannerSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            image_file = request.FILES.get('image')
            if not image_file:
                return Response(
                    {"detail": "No image file provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            banner = ImagebannerModel.objects.create(image=image_file)
            
            response_data = {
                'id': banner.id,
                'image_url': banner.image.url if banner.image else None
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class ImagebannerUpdateAPIView(generics.UpdateAPIView):
    queryset = ImagebannerModel.objects.all()
    serializer_class = ImagebannerSerializer
    
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            
            image_file = request.FILES.get('image')
            if image_file:
                instance.image = image_file
                instance.save()
            
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
            
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(
                {"message": "User deleted successfully"},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {"message": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class UserListAPIView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class TicketDetailAPIView(APIView):
    def get(self, request, id):
        try:
            ticket = Ticket.objects.get(id=id)
            serializer = TicketSerializer(ticket)
            return Response(serializer.data)
        except Ticket.DoesNotExist:
            return Response(
                {"message": "Ticket not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, id):
        try:
            ticket = Ticket.objects.get(id=id)
            
            # Handle main image
            if 'image' in request.FILES:
                if ticket.image:  # Delete old image if exists
                    ticket.image.delete()
                ticket.image = request.FILES['image']
            
            # Update other fields
            if 'category' in request.data:
                ticket.category = request.data['category']
            if 'name' in request.data:
                ticket.name = request.data['name']
            if 'price' in request.data:
                ticket.price = request.data['price']
            if 'address' in request.data:
                ticket.address = request.data['address']
            if 'description' in request.data:
                ticket.description = request.data['description']
            if 'brand' in request.data:
                ticket.brand = request.data['brand']
            if 'carnumber' in request.data:
                ticket.carnumber = request.data['carnumber']
            
            ticket.save()
            
            # Handle additional images
            if 'additional_images' in request.FILES:
                # Delete old additional images
                ImageTicketModel.objects.filter(ticket=ticket).delete()
                
                # Add new additional images
                for image in request.FILES.getlist('additional_images'):
                    ImageTicketModel.objects.create(
                        ticket=ticket,
                        image=image
                    )
            
            serializer = TicketSerializer(ticket)
            return Response({
                "message": "Ticket updated successfully",
                "ticket": serializer.data
            })
            
        except Ticket.DoesNotExist:
            return Response(
                {"message": "Ticket not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
