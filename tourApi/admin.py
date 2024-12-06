from django.contrib import admin
from .models import (
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


admin.site.register(Tour)
admin.site.register(ImageTourModel)
admin.site.register(Hotel)
admin.site.register(ImageHotelModel)
admin.site.register(Restaurant)
admin.site.register(ImageRestaurantModel)
admin.site.register(Packet)
admin.site.register(ImagePacketModel)
admin.site.register(Guide)
admin.site.register(ImageGuideModel)
admin.site.register(Ticket)
admin.site.register(ImageTicketModel)