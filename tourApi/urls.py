# urls.py
from django.urls import path
from tourApi import views


urlpatterns = [
    # Tour management
    path("tour/list/", views.TourListAPIView.as_view(), name="tour-list"),
    path("tour/create/", views.TourCreateAPIView.as_view(), name="tour-create"),
    path(
        "tour/detail/<int:pk>/", views.TourRetrieveAPIView.as_view(), name="tour-detail"
    ),
    path(
        "tour/update/<int:pk>/", views.TourUpdateAPIView.as_view(), name="tour-update"
    ),
    path(
        "tour/delete/<int:pk>/", views.TourDestroyAPIView.as_view(), name="tour-delete"
    ),
    # Hotel management
    path("hotel/list/", views.HotelListAPIView.as_view(), name="hotel-list"),
    path("hotel/create/", views.HotelCreateAPIView.as_view(), name="hotel-create"),
    path(
        "hotel/detail/<int:pk>/",
        views.HotelRetrieveAPIView.as_view(),
        name="hotel-detail",
    ),
    path(
        "hotel/update/<int:pk>/",
        views.HotelUpdateAPIView.as_view(),
        name="hotel-update",
    ),
    path(
        "hotel/delete/<int:pk>/",
        views.HotelDestroyAPIView.as_view(),
        name="hotel-delete",
    ),
    # Restaurant management
    path(
        "restaurant/list/",
        views.RestaurantListAPIView.as_view(),
        name="restaurant-list",
    ),
    path(
        "restaurant/create/",
        views.RestaurantCreateAPIView.as_view(),
        name="restaurant-create",
    ),
    path(
        "restaurant/detail/<int:pk>/",
        views.RestaurantRetrieveAPIView.as_view(),
        name="restaurant-detail",
    ),
    path(
        "restaurant/update/<int:pk>/",
        views.RestaurantUpdateAPIView.as_view(),
        name="restaurant-update",
    ),
    path(
        "restaurant/delete/<int:pk>/",
        views.RestaurantDestroyAPIView.as_view(),
        name="restaurant-delete",
    ),
    # Packet management
    path(
        "packet/list/",
        views.PacketListAPIView.as_view(),
        name="packet-list",
    ),
    path(
        "packet/create/",
        views.PacketCreateAPIView.as_view(),
        name="packet-create",
    ),
    path(
        "packet/detail/<int:pk>/",
        views.PacketRetrieveAPIView.as_view(),
        name="packet-detail",
    ),
    path(
        "packet/update/<int:pk>/",
        views.PacketUpdateAPIView.as_view(),
        name="packet-update",
    ),
    path(
        "packet/delete/<int:pk>/",
        views.PacketDestroyAPIView.as_view(),
        name="packet-delete",
    ),
    # Guide management
    path(
        "guide/list/",
        views.GuideListAPIView.as_view(),
        name="guide-list",
    ),
    path(
        "guide/create/",
        views.GuideCreateAPIView.as_view(),
        name="guide-create",
    ),
    path(
        "guide/detail/<int:pk>/",
        views.GuideRetrieveAPIView.as_view(),
        name="guide-detail",
    ),
    path(
        "guide/update/<int:pk>/",
        views.GuideUpdateAPIView.as_view(),
        name="guide-update",
    ),
    path(
        "guide/delete/<int:pk>/",
        views.GuideDestroyAPIView.as_view(),
        name="guide-delete",
    ),
    # Ticket management
    path("ticket/create/", views.TicketCreateAPIView.as_view(), name="ticket-create"),
    path("tickets/", views.TicketListAPIView.as_view(), name="ticket-list"),
    path("ticket/<int:id>/", views.TicketDetailAPIView.as_view(), name="ticket-detail"),
    # manage site main
    path("sitemain/list/", views.SitemainListAPIView.as_view(), name="sitemain-list"),
    path(
        "sitemain/create/",
        views.SitemainCreateAPIView.as_view(),
        name="sitemain-create",
    ),
    path(
        "sitemain/detail/<int:pk>/",
        views.SitemainRetrieveAPIView.as_view(),
        name="sitemain-detail",
    ),
    path(
        "sitemain/update/<int:pk>/",
        views.SitemainUpdateAPIView.as_view(),
        name="sitemain-update",
    ),
    path(
        "sitemain/delete/<int:pk>/",
        views.SitemainDestroyAPIView.as_view(),
        name="sitemain-delete",
    ),
    path('imagebanner/create/', views.ImagebannerCreateAPIView.as_view(), name='imagebanner-create'),
    path('imagebanner/update/<int:pk>/', views.ImagebannerUpdateAPIView.as_view(), name='imagebanner-update'),
    path('users/<int:pk>/delete/', views.UserDestroyAPIView.as_view(), name='user-delete'),
    path('users/list/', views.UserListAPIView.as_view(), name='user-list'),
]
