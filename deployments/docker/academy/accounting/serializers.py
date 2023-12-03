from rest_framework import serializers
from .models import Plans, Subscriber, Content

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
