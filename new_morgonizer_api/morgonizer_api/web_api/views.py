from django.shortcuts import render
from rest_framework import generics
from web_api.serializers import EventPlaceDetailSerializer, EventPlaceListSerializer, EventPlaceSeatTypeDetailSerializer
from web_api.models import EventPlace, EventPlaceSeatType


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

"""
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
renderer_classes = (TemplateHTMLRenderer, JSONRenderer)

    def get(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            return Response({'EventPlace': self.object}, template_name='event_place_detail.html')
        else:
            return Response({'EventPlace': self.queryset.get(id=1)}) """

