from django.contrib import admin
from django.urls import path, include
from . import views
from web_api.views import *
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title="morgonizer docs/swagger")


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
    path('api_docs/', schema_view),
    path('event/<int:event_id>', views.event),
    path('buy_item/', views.buy_item),
    path('ticket_bought/', views.ticket),
    path('return_form/', views.return_form),
    path('return_ticket/', views.return_ticket),
]