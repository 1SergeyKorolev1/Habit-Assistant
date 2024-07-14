# Generated by Django 5.0.7 on 2024-07-14 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=150, null=True, verbose_name='Место выполнения')),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='Время начала выполнения')),
                ('action', models.CharField(max_length=150, verbose_name='Действие')),
                ('nice_habit_bool', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('periodicity', models.IntegerField(default=1, verbose_name='периодичность напоминания в днях')),
                ('reward', models.CharField(blank=True, max_length=150, null=True, verbose_name='Вознаграждение')),
                ('duration', models.TimeField(blank=True, null=True, verbose_name='Продолжительность выполнения')),
                ('published_bool', models.BooleanField(default=True, verbose_name='Признак публичности')),
                ('connection_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
