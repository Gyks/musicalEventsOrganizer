from django.db import models

class UserAccount(models.Model):
    user_account_name = models.CharField(max_length=128, unique=True) # Аккаунт.
    user_name = models.TextField() # ФИО
    email = models.EmailField()
    admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name}'

class EventPlace(models.Model):
    name = models.CharField('EventPlace Name', max_length=128)
    adress = models.TextField()
    open_air = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class EventPlaceSeatType(models.Model):
    name = models.CharField(max_length=128)
    event_place = models.ForeignKey(EventPlace, on_delete=models.CASCADE)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.event_place.name} - {self.name} : {self.capacity}'

class Contract(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()
    estimated_profit = models.FloatField()
    expenses = models.FloatField()
    event_title = models.CharField(max_length=160)
    event_cover = models.TextField()
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    event_place = models.ForeignKey(EventPlace, on_delete=models.CASCADE)

    def __str__(self):
        return f'Контракт для {self.event_title} в {self.event_date}'

class Ticket(models.Model):
    cost = models.FloatField()
    purchased = models.BooleanField(default=False)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    eventPlace_seatType = models.ForeignKey(EventPlaceSeatType, on_delete=models.CASCADE)

    def __str__(self):
        return f'Билет N:{self.id}-{self.contract.id}-{self.eventPlace_seatType.id}'
