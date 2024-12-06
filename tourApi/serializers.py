# serializers.py
from rest_framework import serializers
from .models import (
    Sitemain,
    ImagebannerModel,
    Tour,
    ImageTourModel,
    Hotel,
    ImageHotelModel,
    Restaurant,
    ImageRestaurantModel,
    Ticket,
    ImageTicketModel,
    Packet,
    ImagePacketModel,
    Guide,
    ImageGuideModel,
)
from django.contrib.auth.models import User


class SitemainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagebannerModel
        fields = "__all__"


class SitemainSerializer(serializers.ModelSerializer):
    banners = serializers.SerializerMethodField()

    def get_banners(self, obj):
        banners = ImagebannerModel.objects.filter(banner=obj)
        serializer = SitemainBannerSerializer(banners, many=True)
        return [i["image"] for i in serializer.data]

    class Meta:
        model = Sitemain
        fields = ["id", "banners", "logo"]


class SitemainCreateSerializer(serializers.ModelSerializer):
    banners = serializers.ListField(child=serializers.ImageField(), required=False)

    class Meta:
        model = Sitemain
        fields = ["id", "banners", "logo"]

    def create(self, validated_data):
        banners_data = validated_data.pop("banners", [])

        sitemain = Sitemain.objects.create(**validated_data)

        for image_file in banners_data:
            image = ImagebannerModel.objects.create(sitemain=sitemain, image=image_file)

        return sitemain

    def update(self, instance, validated_data):
        banners_data = validated_data.pop("banners", [])

        # Update Sitemain fields
        instance.logo = validated_data.get("logo", instance.logo)

        instance.save()

        if banners_data:
            # Clear existing banner if any
            ImagebannerModel.objects.filter(sitemain=instance).delete()
            # Add new banner
            for image_file in banners_data:
                ImagebannerModel.objects.create(sitemain=instance, image=image_file)

        return instance


# Tour Serialisers
class ImageTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTourModel
        fields = "__all__"


class TourSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImageTourModel.objects.filter(tour=obj)
        serializer = ImageTourSerializer(images, many=True)
        return [i["image"] for i in serializer.data]

    class Meta:
        model = Tour
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
            "price",
            "address",
        ]


class TourCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=False)

    class Meta:
        model = Tour
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
            "price",
            "address",
        ]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        tour = Tour.objects.create(**validated_data)
        for image_file in images_data:
            ImageTourModel.objects.create(tour=tour, image=image_file)
        return tour

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", [])

        # Update Tour fields
        instance.category = validated_data.get("category", instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.address = validated_data.get("address", instance.address)
        instance.save()

        if images_data:
            # Clear existing images if any
            ImageTourModel.objects.filter(tour=instance).delete()
            # Add new images
            for image_file in images_data:
                ImageTourModel.objects.create(tour=instance, image=image_file)

        return instance


# Hotel Serialisers
class ImageHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageHotelModel
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImageHotelModel.objects.filter(hotel=obj)
        serializer = ImageHotelSerializer(images, many=True)
        return [i["image"] for i in serializer.data]

    class Meta:
        model = Hotel
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
            "price",
            "address",
        ]


class HotelCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=False)

    class Meta:
        model = Hotel
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
            "price",
            "address",
        ]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        hotel = Hotel.objects.create(**validated_data)
        for image_file in images_data:
            ImageHotelModel.objects.create(hotel=hotel, image=image_file)
        return hotel

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", [])

        # Update Hotel fields
        instance.category = validated_data.get("category", instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.address = validated_data.get("address", instance.address)
        instance.save()

        if images_data:
            # Clear existing images if any
            ImageHotelModel.objects.filter(hotel=instance).delete()
            # Add new images
            for image_file in images_data:
                ImageHotelModel.objects.create(hotel=instance, image=image_file)

        return instance


# Restaurant Serialisers
class ImageRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRestaurantModel
        fields = "__all__"


class RestaurantSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImageRestaurantModel.objects.filter(restaurant=obj)
        serializer = ImageRestaurantSerializer(images, many=True)
        return [i["image"] for i in serializer.data]

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
            "address",
        ]


class RestaurantCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=False)

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
            "address",
        ]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        restaurant = Restaurant.objects.create(**validated_data)
        for image_file in images_data:
            ImageRestaurantModel.objects.create(restaurant=restaurant, image=image_file)
        return restaurant

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", [])

        # Update Restaurant fields
        instance.category = validated_data.get("category", instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.description = validated_data.get("description", instance.description)
        instance.address = validated_data.get("address", instance.address)
        instance.save()

        if images_data:
            # Clear existing images if any
            ImageRestaurantModel.objects.filter(restaurant=instance).delete()
            # Add new images
            for image_file in images_data:
                ImageRestaurantModel.objects.create(
                    restaurant=instance, image=image_file
                )

        return instance


# Packet Serialisers
class ImagePacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePacketModel
        fields = "__all__"


class PacketSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImagePacketModel.objects.filter(packet=obj)
        serializer = ImagePacketSerializer(images, many=True)
        return [i["image"] for i in serializer.data]

    class Meta:
        model = Packet
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
            "price",
            "address",
        ]


class PacketCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=False)

    class Meta:
        model = Packet
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
            "price",
            "address",
        ]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        packet = Packet.objects.create(**validated_data)
        for image_file in images_data:
            ImagePacketModel.objects.create(packet=packet, image=image_file)
        return packet

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", [])

        # Update Packet fields
        instance.category = validated_data.get("category", instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.address = validated_data.get("address", instance.address)
        instance.save()

        if images_data:
            # Clear existing images if any
            ImagePacketModel.objects.filter(packet=instance).delete()
            # Add new images
            for image_file in images_data:
                ImagePacketModel.objects.create(packet=instance, image=image_file)

        return instance


# Guide Serialisers
class ImageGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGuideModel
        fields = "__all__"


class GuideSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImageGuideModel.objects.filter(guide=obj)
        serializer = ImageGuideSerializer(images, many=True)
        return [i["image"] for i in serializer.data]

    class Meta:
        model = Guide
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
        ]


class GuideCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=False)

    class Meta:
        model = Guide
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
        ]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        guide = Guide.objects.create(**validated_data)
        for image_file in images_data:
            ImageGuideModel.objects.create(guide=guide, image=image_file)
        return guide

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", [])

        # Update Guide fields
        instance.category = validated_data.get("category", instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.description = validated_data.get("description", instance.description)
        instance.save()

        if images_data:
            # Clear existing images if any
            ImageGuideModel.objects.filter(guide=instance).delete()
            # Add new images
            for image_file in images_data:
                ImageGuideModel.objects.create(guide=instance, image=image_file)

        return instance


class ImageTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTicketModel
        fields = ['id', 'image']


class TicketSerializer(serializers.ModelSerializer):
    additional_images = ImageTicketSerializer(many=True, read_only=True, source='imageticketmodel_set')
    
    class Meta:
        model = Ticket
        fields = [
            'id',
            'category',
            'name',
            'image',
            'description',
            'address',
            'price',
            'brand',
            'carnumber',
            'additional_images'
        ]


class TicketCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=False)

    class Meta:
        model = Ticket
        fields = [
            "id",
            "category",
            "name",
            "image",
            "images",
            "description",
            "address",
            "price",
            "brand",
            "carnumber",
        ]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])

        ticket = Ticket.objects.create(**validated_data)

        for image_file in images_data:
            image = ImageTicketModel.objects.create(ticket=ticket, image=image_file)

        return ticket

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", [])

        # Update Ticket fields
        instance.category = validated_data.get("category", instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.address = validated_data.get("address", instance.address)
        instance.brand = validated_data.get("brand", instance.brand)
        instance.carnumber = validated_data.get("carnumber", instance.carnumber)
        instance.save()

        if images_data:
            # Clear existing images if any
            ImageTicketModel.objects.filter(ticket=instance).delete()
            # Add new images
            for image_file in images_data:
                ImageTicketModel.objects.create(ticket=instance, image=image_file)

        return instance


class ImagebannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagebannerModel
        fields = ['id', 'image', 'created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
