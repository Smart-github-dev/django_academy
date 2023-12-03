from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('signup/<int:id>', views.signup, name='signup'),
    path('password/', views.change_password, name='edit-password'),
    path('contact', views.contact, name='contact'),
    path('contact-success', views.contact_success, name='contact_success'),
    path('user-questions',views.user_questions, name='contact_review'),
    path('faq',views.faq,name='faq'),
    path('links', views.links_view, name='links'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('forbidden', views.forbidden, name='forbidden'),
    path('test', views.test, name='test'),
]
