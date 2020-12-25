from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """ Conversation Admin """

    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ Model Admin """

    pass