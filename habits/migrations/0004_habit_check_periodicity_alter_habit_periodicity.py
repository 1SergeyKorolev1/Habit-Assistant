# Generated by Django 5.0.7 on 2024-07-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='check_periodicity',
            field=models.IntegerField(default=0, verbose_name='проверка периодичности'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.IntegerField(default=3, verbose_name='периодичность напоминания в днях'),
        ),
    ]
