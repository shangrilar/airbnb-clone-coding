from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """ Conversation Admin """

    list_display = (
        "__str__",
        "count_participants",
        "count_messages",
    )


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ Model Admin """

    list_display = ("__str__", "created")