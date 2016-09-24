from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class EnhancedUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to="images/avatars", default='images/avatar/default.jpg')


class Conversation(models.Model):

    sender = models.ForeignKey(EnhancedUser, related_name="sender")
    receiver = models.ForeignKey(EnhancedUser, related_name="receiver")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class SocialType(models.Model):

    name = models.CharField(max_length=100, primary_key=True)


class SocialNetwork(models.Model):

    link = models.URLField(unique=True)
    name = models.OneToOneField(SocialType)
    user = models.OneToOneField(User)


class Announce(models.Model):

    location = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    #todo create user folder for announce pictures


class AnnouncePicture(models.Model):

    user = models.OneToOneField(EnhancedUser)
    announce = models.ForeignKey(Announce)
    picture = models.ImageField(upload_to="images/announce", null=False)


class AnimalType(models.Model):

    race = models.CharField(max_length=50, primary_key=True)


class Animal(models.Model):

    size = models.TextField()
    breed = models.TextField()
    color = models.TextField()
    description = models.TextField(null=True)
    name = models.TextField(null=True)
    announce = models.ForeignKey(Announce)


