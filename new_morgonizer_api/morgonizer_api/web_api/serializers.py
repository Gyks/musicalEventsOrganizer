from rest_framework import serializers
from web_api.models import EventPlace, EventPlaceSeatType, Contract, Ticket


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


class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ContractDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class TicketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'