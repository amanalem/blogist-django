from django.contrib import admin
from .models import Post, Comment, Message, Reply


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Reply)
