from django.shortcuts import render
from rest_framework import generics
from web_api.serializers import *
from web_api.models import EventPlace, EventPlaceSeatType, Contract, Ticket
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt



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


def index(request):
    latest_contracts_list = Contract.objects.all().order_by('-created')[0:5]
    context = {'latest_contracts_list': latest_contracts_list}
    return render(request, 'index.html', context)


def event_place(request):
    latest_event_place_list = EventPlace.objects.all()[0:5]
    context = {'latest_event_place_list': latest_event_place_list}
    return render(request, 'event_place.html', context)


def event(request, event_id):
    contract = get_object_or_404(Contract, id=event_id)
    event_place_id = contract.event_place.id
    seat_types = EventPlaceSeatType.objects.filter(event_place=event_place_id)
    ticket_seat_type = []
    tickets_count = []
    for item in seat_types:
        tickets = Ticket.objects.filter(eventPlace_seatType=item.id, contract=event_id)
        if tickets:
            ticket_seat_type.append(
                (
                    tickets[0].cost, 
                    item,
                    Ticket.objects.filter(eventPlace_seatType=item.id, contract=event_id, purchased=False).count(),
                    )
                )            
    context = {
        'contract': contract,
        'ticket_seat_type': ticket_seat_type,
        }
    return render(request, 'event.html', context)


def buy_item(request):
    if request.method == "GET":
        seat_type = get_object_or_404(EventPlaceSeatType, id=request.GET['seat_type'])
        contract = get_object_or_404(Contract, id=request.GET['contract'])
        ticket = Ticket.objects.filter(eventPlace_seatType=seat_type.id, contract=contract.id, purchased=False)[0]
        context = {'seat_type': seat_type, 'contract': contract, 'ticket': ticket}
        return render(request, 'buy_item.html', context)
    else:
        return JsonResponse({'error':'incorrect request'})


def ticket(request):
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        ticket = get_object_or_404(Ticket, id=request.POST['ticket_id'])
        if ticket.purchased == True:
            return HttpResponse("Этот билет уже куплен.")
        ticket.buyer_email = email
        ticket.buyer_mobile = phone
        ticket.purchased = True
        ticket.save()
        context = {
            'email': email,
            'phone': phone,
            'ticket': ticket,
        }
        return render(request, 'ticket.html', context)


def return_ticket(request):
    if request.method == "POST":
        # ticket = get_object_or_404(Ticket, id=)
        try:
            ticket = Ticket.objects.get(pk=request.POST['ticket_id'])
        except:
            return HttpResponse("Неккоректный номер билета или email")
        email = request.POST['email']
        if email == ticket.buyer_email:
            ticket.buyer_email = ""
            ticket.buyer_mobile = ""
            ticket.purchased = False
            ticket.save()
            return HttpResponse("<h1>Успешный возврат билета.</h1>")
    return HttpResponse("Неккоректный номер билета или email")


def return_form(request):
    context = {}
    return render(request, 'return_form.html', context)


def search(request):
    query = request.GET['search']
    if query:
        event_places = EventPlace.objects.filter(name__icontains=query)
        contracts = Contract.objects.filter(event_title__icontains=query)
    else:
        event_places = contracts = []
    context = { 
        'query': query, 
        'event_places': event_places, 
        'contracts': contracts,
    }
    return render(request, 'search.html', context)