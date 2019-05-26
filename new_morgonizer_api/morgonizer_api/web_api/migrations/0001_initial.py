# Generated by Django 2.2.1 on 2019-05-25 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateTimeField()),
                ('estimated_profit', models.FloatField()),
                ('expenses', models.FloatField()),
                ('event_title', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='EventPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='EventPlace Name')),
                ('adress', models.TextField()),
                ('open_air', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EventPlaceSeatType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('event_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.EventPlace')),
            ],
        ),
        migrations.CreateModel(
            name='SeatType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_account_name', models.CharField(max_length=128, unique=True)),
                ('user_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('purchased', models.BooleanField(default=False)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.Contract')),
                ('eventPlace_seatType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.EventPlaceSeatType')),
            ],
        ),
        migrations.AddField(
            model_name='eventplaceseattype',
            name='seat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.SeatType'),
        ),
        migrations.AddField(
            model_name='contract',
            name='event_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.EventPlace'),
        ),
        migrations.AddField(
            model_name='contract',
            name='user_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.UserAccount'),
        ),
    ]