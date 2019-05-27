from rest_framework import serializers
from web_api.models import EventPlace, EventPlaceSeatType

class EventPlaceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPlace
        fields = '__all__'


class EventPlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPlace
        fields = ('id', 'name', 'adress')


class EventPlaceSeatTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPlaceSeatType
        fields = '__all__'