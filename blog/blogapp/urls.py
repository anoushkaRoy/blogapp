from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blogs/create/', views.blog_create, name='blog_create'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blogs/<int:pk>/update/', views.blog_update, name='blog_update'),
    path('blogs/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('blogs/<int:blog_pk>/subblogs/create/', views.subblog_create, name='subblog_create'),
]
