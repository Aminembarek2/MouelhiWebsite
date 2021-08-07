from django.db import models
from django import forms
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/', default='')
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.date)

class Video(models.Model):
    title = models.CharField(max_length=100,default=True)
    video_url = models.URLField(max_length=10000000000,blank=True, null=True,default='')
    video = models.FileField(upload_to='videos/',blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    image = models.ImageField(upload_to='videos/Thumb/',null=True)

    def __str__(self):
        return self.title
