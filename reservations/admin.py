from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ Reservation Admin """

    list_display = (
        "room",
        "status",
        "guest",
        "check_in",
        "check_out",
        "check_in_progress",
    )

    list_filter = ("status",)
