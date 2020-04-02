from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups:main_group', kwargs={'pk':self.pk})

class GroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, models.CASCADE)

    def __str__(self):
        return self.user.username
    
    