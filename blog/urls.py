from django.urls import path
from . import views


urlpatterns = [
    path('', views.display_blogcontent, name="blog"),
    path('<str:slug>', views.blog_post, name="blog_post"),
]
