from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.HouseRule, models.Amenity, models.Facility)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin """

    pass


@admin.register(models.Room)
class CustomRoomAdmin(admin.ModelAdmin):
    """ Custom Room Admin """

    pass