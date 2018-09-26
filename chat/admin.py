from django.contrib import admin
from .models import Message, Conversation


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'sender', 'message', 'sent_date')


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sender', 'recipient', 'conversation_date')


admin.site.register(Message, MessagesAdmin)
admin.site.register(Conversation, ConversationAdmin)
