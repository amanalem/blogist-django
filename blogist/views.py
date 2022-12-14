from ast import Delete
from django.http import JsonResponse
from django.shortcuts import render
from blogist import serializers
from blogist.apps import BlogistConfig
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StyleSerializer, UserSerializer, PostSerializer, CommentSerializer, ReplySerializer, MessageSerializer
from .models import Post, Comment, Reply, Message, Style
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
User = get_user_model()


# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration Successful'})
        return Response({'message': serializer.errors}, status=422)


class LoginView(APIView):
    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid Credentials'})

    def post(self, request):
        email = request.data.get('email')
        # password = request.data.get('password')

        user = self.get_user(email)
        serializer = UserSerializer(user)
        if not serializer.validate(request.data):
            raise PermissionDenied({'message': 'Invalid Credentials'})

        token = jwt.encode(
            {'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')

        return Response({'token': token, 'user': user, 'message': f'Welcome {user.username} {user.last_name}'})


class BlogistView(APIView):
    def get(self, request):
        blogist = User.objects.get(is_superuser=True)
        serializer = UserSerializer(blogist)
        return Response(serializer.data)


class PostsView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        # post_data = JSONParser().parse(request)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=422)


class PostDetailView(APIView):
    def get(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({"message": "Post Deleted"})

    def put(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=422)


class CommentsView(APIView):
    def get(self, request, pk, format=None):
        comments = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=422)


class CommentDetailView(APIView):
    def delete(self, request, pk, format=None):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response({"message": "Comment Deleted"})


class RepliesView(APIView):
    def get(self, request, pk, format=None):
        replies = Reply.objects.filter(comment=pk)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=422)


class StyleView(APIView):
    def get(self, request):
        style = Style.objects.first()
        serializer = StyleSerializer(style)
        return Response(serializer.data)

    def post(self, request):
        serializer = StyleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=422)

    def put(self, request):
        style = Style.objects.first()
        serializer = StyleSerializer(style, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=422)
