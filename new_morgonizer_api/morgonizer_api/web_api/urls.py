from django.contrib import admin
from django.urls import path, include
from . import views
from web_api.views import *


api_prefix = 'api/v1/'

urlpatterns = [
    path(api_prefix + 'event_place/create', EventPlaceCreateView.as_view()),
    path(api_prefix + 'event_place/all', EventPlaceListView.as_view()),
    path(api_prefix + 'event_place/detail/<int:pk>', EventPlaceDetailView.as_view()),
    path(api_prefix + 'event_place/seat_type/create', EventPlaceSeatTypeCreateView.as_view()),
    path(api_prefix + 'event_place/seat_type/detail/<int:pk>', EventPlaceSeatTypeDetailView.as_view()),
    path(api_prefix + 'contract/all', ContractListView.as_view()),
    path(api_prefix + 'contract/create', ContractCreateView.as_view()),
    path(api_prefix + 'contract/detail/<int:pk>', ContractDetailView.as_view()),
    path(api_prefix + 'ticket/detail/<int:pk>', TicketDetailView.as_view()),
    path(api_prefix + 'ticket/create', TicketCreateView.as_view()),
    path(api_prefix + 'get_seat_types/<int:event_place_id>', views.event_place_seat_type),
    path(api_prefix + 'create_tickets', views.create_tickets),
    path('', views.index),
    path('event_place/', views.event_place),
    path('event/<int:event_id>', views.event),
]