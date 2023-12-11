from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "mentors"

urlpatterns = [
    path("", views.mentor_dashboard, name="mentors"),
    path("dashboard", views.mentor_dashboard, name="mentors_dashboard"),
    path("history", views.mentor_history, name="mentor_history"),
    path("paypal", views.mentor_payPal, name="mentor_paypal"),
    path("mentor_changes", views.mentor_changes, name="mentor_changes"),
    path("update_user", views.mentor_update_user, name="mentor_update_user"),
    path(
        "manage_user/details",
        views.mentor_user_info_details,
        name="mentor_user_details",
    ),
    path("manage_user", views.mentor_manage_user, name="mentor_manage_user"),
    path(
        "update_status_change", views.update_status_change, name="update_status_change"
    ),
    path(
        "github_activitys",
        views.github_activitys,
        name="github_activitys",
    ),
    path("recent_subscribers", views.recent_subscribers, name="recent_subscribers"),
]
