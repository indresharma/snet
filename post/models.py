from django.db import models
from django.conf import settings
from django.urls import reverse
from groups.models import Group, GroupMember

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', default=0)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

    

 


