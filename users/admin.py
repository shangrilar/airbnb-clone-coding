from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_model


class RoomInline(admin.TabularInline):

    model = room_model.Room


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    inlines = (RoomInline,)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

    list_filter = UserAdmin.list_filter + ("superhost",)