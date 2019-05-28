from django.contrib import admin
from django.urls import path, include
from web_api.views import *


urlpatterns = [
    path('event_place/create', EventPlaceCreateView.as_view()),
    path('event_place/all', EventPlaceListView.as_view()),
    path('event_place/detail/<int:pk>', EventPlaceDetailView.as_view()),
    path('event_place/seat_type/create', EventPlaceSeatTypeCreateView.as_view()),
    path('event_place/seat_type/detail/<int:pk>', EventPlaceSeatTypeDetailView.as_view())
]
