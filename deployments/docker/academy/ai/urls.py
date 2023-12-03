from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('chat', views.ai_chat, name='chat-main'),
    path('chat_interview', views.ai_chat_interview, name='interview'),
    path('chatbox_start', views.ai_chatbox_start, name='chatbox_start'),
    path('chatbox_dialog', views.ai_chatbox_dialog, name='chatbox_dialog'),
    path('', views.ai_view, name='ai'),
]
