from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('folders/', views.videos, name='folders'),
    path('folders/<str:resource_key>', views.videos, name='folders'),
    path('watch/<str:key>', views.watch, name='video'),
    path('recent/', views.recent_videos, name='recent_videos'),
    path('search/', views.search_videos, name='search-video'),
    path('get-ajex-tree/', views.get_ajax_tree, name='get-ajex-tree'),
    path('get-child-or-video/<str:resource_key>', views.get_child_or_video, name='get-videos'),
]
