from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.subscription, name='subscription'),
    path('<int:plan_id>/learn-more', views.learn_more, name='learn-more'),
    path('process', views.process, name='process'),
    path('success',views.success_payment, name='success'),
    path('complete', views.payment_complete, name='complete'),
    path('cancel', views.cancel_subscription, name='cancel'),
    path('declined', views.declined_payment, name='declined'),
    path('transactions/<str:username>', views.transactions, name='transactions'),
    path('terms-and-conditions',views.terms_of_condition, name='terms-and-conditions'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),
]
