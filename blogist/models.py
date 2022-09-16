from operator import mod
from statistics import mode
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Post(models.Model):
    media = models.TextField()
    media_alt = models.CharField(max_length=100, default='No alt text')
    title = models.CharField(max_length=100)
    body = models.TextField()

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=200)

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )

    def __str__(self) -> str:
        return f'{self.post} - {self.author}'


class Reply(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=200)

    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies'
    )

    def __str__(self) -> str:
        return f'{self.author} on: {self.comment}'


class Message(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages'
    )
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.author


class Style(models.Model):
    title = models.CharField(max_length=100)
    title_align = models.CharField(max_length=50, default='center')
    about = models.TextField()
    about_img = models.TextField()
    about_bg_color = models.CharField(max_length=50)
    about_txt_color = models.CharField(max_length=50)
    blog_bg_img = models.TextField()
    blog_bg_color = models.CharField(max_length=50)
    blog_txt_color = models.CharField(max_length=50)
