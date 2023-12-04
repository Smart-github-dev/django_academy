from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.mentorDashboard, name='mentors'),
    path('dashboard', views.mentorDashboard, name='mentors-dashboard'),
    path("history",views.mentorHistory,name="mentor_history"),
    path("paypal",views.mentorPayPal,name="mentor_paypal"),
    path("mentor_changes",views.mentorChanges,name="mentor_changes"),
    path("updateuser",views.mentorUpdateUser,name="mentor_update_user"),
    path("userinfos",views.mentorUserInfo,name="mentor_user_infos"),
    path("userinfos/details",views.mentorUserInfoDetails,name="mentor_user_details"),
    path("accesscontrol",views.mentorAccessControl,name="mentor_access_control"),
    path("manageuser",views.mentorManageUser,name="mentor_manage_user")
]
