from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)

    def __str__(self):
        return self.sender.__str__() + " & " + self.recipient.__str__()


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500, blank=True )
    sent_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.conversation.__str__()

    def sender(self):
        return self.sender.__str__()