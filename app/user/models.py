from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(null=True, blank=True, max_length=14)
    nickname = models.CharField(null=True, blank=True, max_length=40)
    img = models.ImageField("img", null=True, blank=True, upload_to="img")
    status = models.CharField(null=True, blank=True, max_length=200)
    address = models.CharField(null=True, blank=True, max_length=200)


class ProfilePhoto(models.Model):
    img = models.ImageField("img", null=True, blank=True, upload_to="img")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True,blank=True)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend")


class CommentProfilePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField()
    photo = models.ForeignKey(ProfilePhoto, on_delete=models.CASCADE, null=True, blank=True)