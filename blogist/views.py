from django.shortcuts import render
from blogist import serializers
from blogist.apps import BlogistConfig
from rest_framework.response import Response
from rest_framework.decorators import blogist_view
from .serializers import UserSerializer, PostSerializer, CommentSerializer, ReplySerializer, MessageSerializer
from .models import Post, Comment, Reply, Message
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
User = get_user_model()


# Create your views here.
