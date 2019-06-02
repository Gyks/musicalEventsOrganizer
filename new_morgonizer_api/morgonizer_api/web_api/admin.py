from .models import UserAccount, EventPlace, EventPlaceSeatType, Contract, Ticket
from django.contrib.auth.models import Group
from django.contrib import admin
from django import forms


class EventPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'adress', 'open_air')
    list_filter = ('name',)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_date', 'event_place')
    change_form_template = 'admin/contract_forms.html'


admin.site.site_header = 'Панель управления:'
admin.site.register(UserAccount)
admin.site.register(EventPlace, EventPlaceAdmin)
admin.site.register(EventPlaceSeatType)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Ticket)
admin.site.unregister(Group)