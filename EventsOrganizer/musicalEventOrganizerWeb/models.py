from django.db import models

# Create your models here.

class UserAccount(models.Model):
    account_name = models.models.TextField(unique=True)
    name = models.CharField(max_length=50)
    password_hash = models.TextField()
    manager = models.BooleanField()


class Contract(models.Model):
    created_date = models.DateTimeField()
    last_updated_date = models.DateTimeField()
    estimated_profit = models.FloatField()
    exoenses = models.FloatField()
    manager_id = models.IntegerField() # must be unique, taken from user_account
    evente_title = models.TextField()


class Contract_EventPlace(models.Model):
    contract_id = models.IntegerField()
    EventPlace_id = models.IntegerField()


class EventPlace(models.Model):
    name = models.TextField()
    adress = models.CharField(max_length=80)
    open_air = models.BooleanField()
    event_date = models.DateTimeField()


class Ticket(models.Model):
    ContractEventPlace_id = models.IntegerField()


class SeatType(models.Model):
    name = models.CharField(80)


class Place_SeatType(models.Model):
    EventPlace_id = models.IntegerField()
    SeatType_id = models.IntegerField()
    capacity = models.IntegerField()
    cost = models.IntegerField()