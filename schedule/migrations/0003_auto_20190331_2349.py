# Generated by Django 2.1.5 on 2019-03-31 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20190321_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date',
        ),
        migrations.AddField(
            model_name='schedule',
            name='date_and_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]