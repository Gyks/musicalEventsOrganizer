# Generated by Django 2.2.1 on 2019-05-25 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventplaceseattype',
            name='seat_type',
        ),
        migrations.AddField(
            model_name='eventplaceseattype',
            name='name',
            field=models.CharField(default='new', max_length=128),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SeatType',
        ),
    ]