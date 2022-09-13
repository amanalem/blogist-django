from django.http import JsonResponse
from django.shortcuts import render
from blogist import serializers
from blogist.apps import BlogistConfig
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, PostSerializer, CommentSerializer, ReplySerializer, MessageSerializer
from .models import Post, Comment, Reply, Message
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
User = get_user_model()


# Create your views here.

class RegisterView(APIView):
    def post(self, req):
        serializer = UserSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration Successful'})
        return Response(serializer.errors, status=422)


class LoginView(APIView):
    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid Credentials'})

    def post(self, req):
        email = req.data.get('email')
        password = req.data.get('password')

        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid Credentials'})

        token = jwt.encode(
            {'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')

        return Response({'token': token, 'message': f'Welcome {user.username}'})


class PostsView(APIView):
    def get(self, req):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, req):
        serializer = PostSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'New Post Created!'})
        return Response(serializer.errors, status=422)
