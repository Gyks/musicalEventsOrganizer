from django.db import models

class UserAccount(models.Model):
    user_account_name = models.CharField('Имя аккаунта в django:', max_length=128, unique=True) # Аккаунт.
    user_name = models.TextField('ФИО') # ФИО
    email = models.EmailField()
    admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name}'

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

class EventPlace(models.Model):
    name = models.CharField('Название площадки', max_length=128)
    adress = models.TextField('Адрес:')
    open_air = models.BooleanField('Открытая:', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'


class EventPlaceSeatType(models.Model):
    name = models.CharField('Имя:', max_length=128)
    event_place = models.ForeignKey(EventPlace, on_delete=models.CASCADE)
    capacity = models.IntegerField('Вместимость:')

    class Meta:
        verbose_name = 'Тип места для площадок'
        verbose_name_plural = 'Типы мест для площадок'

    def __str__(self):
        return f'{self.event_place.name} - {self.name} : {self.capacity}'

class Contract(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField('Дата события:')
    estimated_profit = models.FloatField('Ожидаемая прибыль:')
    expenses = models.FloatField('Ожидаемые затраты:')
    event_title = models.CharField('Название события:', max_length=160)
    event_cover = models.TextField('Ссылка на картинку для события:')
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    event_place = models.ForeignKey(EventPlace, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'

    def __str__(self):
        return f'Контракт для {self.event_title} в {self.event_date}'

class Ticket(models.Model):
    cost = models.FloatField()
    buyer_email = models.CharField(max_length=160)
    buyer_mobile = models.CharField(max_length=160)
    purchased = models.BooleanField(default=False)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    eventPlace_seatType = models.ForeignKey(EventPlaceSeatType, on_delete=models.CASCADE)

    def __str__(self):
        return f'Билет N:{self.id}-{self.contract.id}-{self.eventPlace_seatType.id}'
    
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
