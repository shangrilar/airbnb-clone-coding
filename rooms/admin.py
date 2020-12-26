from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.HouseRule, models.Amenity, models.Facility)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50px' src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class CustomRoomAdmin(admin.ModelAdmin):
    """ Custom Room Admin """

    inlines = (PhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "host",
                )
            },
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "Space",
            {"fields": ("guests", "beds", "bedrooms", "baths")},
        ),
        (
            "More about the Spaces",
            {
                "fields": ("amenities", "house_rules", "facilities"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "total_rating",
        "count_photo",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "house_rules",
        "facilities",
        "city",
        "country",
    )

    search_fields = ("city", "host__username")

    filter_horizontal = (
        "amenities",
        "house_rules",
        "facilities",
    )

    raw_id_fields = ("host",)