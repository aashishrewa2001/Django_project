# models.py
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    tagline = models.CharField(max_length=200)
    schedule = models.DateTimeField()
    description = models.TextField()
    moderator = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    rigor_rank = models.IntegerField()
    attendees = models.ManyToManyField(User, related_name='attended_events', blank=True)

    # def __str__(self):
    #     return self.name
