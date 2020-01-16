from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListViews , PostDetailViews , PostCreateViews , PostUpdateViews , PostDeleteViews , UserPostListViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListViews.as_view() , name='blog-home'),
    # path('', views.home , name='blog-home'),
    path('post/<int:pk>/', PostDetailViews.as_view() , name='post-detail'),
    path('post/new/', PostCreateViews.as_view() , name='post-create'),
    path('post/<int:pk>/update/', PostUpdateViews.as_view() , name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteViews.as_view() , name='post-delete'),
    path('about/', views.about , name='blog-about'),
    path('user/<str:username>', UserPostListViews.as_view() , name='user-posts'),
]
