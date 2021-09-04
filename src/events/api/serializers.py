from django.db.models import fields
from rest_framework import serializers
from events.models import Event, SubscribeEmail, Order

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = '__all__'


class SubscribeEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscribeEmail
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'