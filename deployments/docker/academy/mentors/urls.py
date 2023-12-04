from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.mentorDashboard, name='mentors'),
    path('dashboard', views.mentorDashboard, name='mentors-dashboard'),
    path("history",views.mentorHistory,name="mentor_history"),
    path("paypal",views.mentorPayPal,name="mentor_paypal"),
    path("mentor_changes",views.mentorChanges,name="mentor_changes"),
    path("update_user",views.mentorUpdateUser,name="mentor_update_user"),
    path("user_infos",views.mentorUserInfo,name="mentor_user_infos"),
    path("user_infos/details",views.mentorUserInfoDetails,name="mentor_user_details"),
    path("access_control",views.mentorAccessControl,name="mentor_access_control"),
    path("manage_user",views.mentorManageUser,name="mentor_manage_user")
]
