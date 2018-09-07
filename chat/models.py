from django.db import models
from landing.models import Stylista


class Conversation(models.Model):
    sender = models.ForeignKey(Stylista, related_name='sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Stylista, related_name='receiver', on_delete=models.CASCADE)

    def __str__(self):
        return self.sender + " & " + self.recipient


class Message(models.Model):
    conversation = models.OneToOneField(Conversation, on_delete=models.CASCADE)
    sender = models.OneToOneField(Stylista, on_delete=models.CASCADE)
    message = models.TextField(max_length=500, blank=True )
    sent_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.conversation

    def sender(self):
        return self.sender