from .models import UserAccount, EventPlace, EventPlaceSeatType, Contract, Ticket
from django.contrib import admin

admin.site.register(UserAccount)
admin.site.register(EventPlace)
admin.site.register(EventPlaceSeatType)
admin.site.register(Contract)
admin.site.register(Ticket)