from django.shortcuts import render
from rest_framework import generics
from web_api.serializers import *
from web_api.models import EventPlace, EventPlaceSeatType, Contract, Ticket

class EventPlaceCreateView(generics.CreateAPIView):
    serializer_class = EventPlaceDetailSerializer


class EventPlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventPlaceDetailSerializer
    queryset = EventPlace.objects.all()


class EventPlaceListView(generics.ListAPIView):
    serializer_class = EventPlaceListSerializer
    queryset = EventPlace.objects.all()


class EventPlaceSeatTypeCreateView(generics.CreateAPIView):
    serializer_class = EventPlaceSeatTypeDetailSerializer


class EventPlaceSeatTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventPlaceSeatTypeDetailSerializer
    queryset = EventPlaceSeatType.objects.all()

class ContractListView(generics.ListAPIView):
    serializer_class = ContractListSerializer
    queryset = Contract.objects.all()


class ContractCreateView(generics.CreateAPIView):
    serializer_class = ContractDetailSerializer


class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContractDetailSerializer
    queryset = Contract.objects.all()


class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketDetailSerializer


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketDetailSerializer
    queryset = Ticket.objects.all()