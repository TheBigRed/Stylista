from django.contrib import admin
from .models import Message, Conversation


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('sender', 'message')


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sender', 'recipient')


admin.site.register(Message, MessagesAdmin)
admin.site.register(Conversation, ConversationAdmin)
