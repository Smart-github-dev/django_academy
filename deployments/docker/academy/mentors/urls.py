from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.mentorDashboard, name='mentors'),
    path('dashboard', views.mentorDashboard, name='mentors-dashboard')
]
