from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name='like_posts', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_posts', blank=True)
    share = models.ManyToManyField(User, related_name='share_posts', blank=True)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

    def __str__(self):
        return F"{self.title}{self.body}"

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return F"{self.author}{self.body}"
    