from django.urls import path
from . import views
from django.views.generic import TemplateView 

urlpatterns = [
    path('', views.profile, name='profile'),
    path('',TemplateView.as_view(template_name='profiles/profile_social.html')),

]
