from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #auto_now / auto_now_add (only when object created : doesnt allow changing dates)
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return f'title: {self.title}'

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.id})