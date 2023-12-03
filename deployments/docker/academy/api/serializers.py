from rest_framework import serializers
from main.models import JsonStore
from accounting.models import Plans, Subscriber, Content


class JsonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JsonStore
        fields = ['name', 'data', 'created_date', 'updated_date']



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
