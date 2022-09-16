from django.urls import path
from . import views

urlpatterns = [
    path('posts-list/', views.PostsView.as_view(), name='posts_list'),
    path('posts-list/<int:pk>/',
         views.PostDetailView.as_view(), name='post_detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('get-admin/', views.BlogistView.as_view(), name='get-admin'),
    path('posts-list/<int:pk>/comments/',
         views.CommentsView.as_view(), name="comments_list"),
    path('replies-list/<int:pk>/',
         views.RepliesView.as_view(), name="replies_list"),
    path('style/', views.StyleView.as_view(), name="style"),
]
