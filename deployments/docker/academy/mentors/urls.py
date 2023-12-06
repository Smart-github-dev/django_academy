from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.mentor_dashboard, name='mentors'),
    path('dashboard', views.mentor_dashboard, name='mentors_dashboard'),
    path("history",views.mentor_history,name="mentor_history"),
    path("paypal",views.mentor_payPal,name="mentor_paypal"),
    path("mentor_changes",views.mentor_changes,name="mentor_changes"),
    path("update_user",views.mentor_update_user,name="mentor_update_user"),
    path("user_infos",views.mentor_user_info,name="mentor_user_infos"),
    path("user_infos/details",views.mentor_user_info_details,name="mentor_user_details"),
    path("access_control",views.mentor_access_control,name="mentor_access_control"),
    path("manage_user",views.mentor_manage_user,name="mentor_manage_user")
]
