from django.db import models
from django.contrib.auth.models import User
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default_pic_profile.jpg", upload_to='profile_pic')
    about_me = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


