from rest_framework import routers, serializers, viewsets
from rest_framework.documentation import include_docs_urls
from main.models import JsonStore
from django.urls import path, include
from api.views import JsonViewSet, PlansViewSet, SubscriberViewSet, ContentViewSet
from api import views

router = routers.DefaultRouter()
router.register(r'json-store', JsonViewSet)
router.register(r'plans', PlansViewSet)
router.register(r'subscribers', SubscriberViewSet)
router.register(r'contents', ContentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='Academy api documentation!!'))
]
