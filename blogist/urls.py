from django.urls import path
from . import views
urlpatterns = [
    path('posts-list/', views.PostsView.as_view(), name='posts_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),

]
