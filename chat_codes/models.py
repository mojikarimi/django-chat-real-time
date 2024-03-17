from django.db import models
from datetime import datetime


# Create your models here.
class ChatRoom(models.Model):
    user = models.CharField(blank=True, max_length=150)
    ip_client = models.CharField(max_length=40, blank=True)
    date = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.user + 'Room'


class ChatMessage(models.Model):
    room_id = models.IntegerField(default=0)
    text = models.TextField(blank=True)
    type = models.CharField(max_length=25, blank=True, choices=(('client', 'client'), ('admin', 'admin')))
    date = models.CharField(max_length=10, default='')
    status = models.BooleanField(default=False)

    def __str__(self):
        return 'Room ID: ' + str(self.room_id)
