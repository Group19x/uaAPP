# Generated by Django 2.1.5 on 2019-03-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_remove_schedule_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date_and_time',
        ),
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='schedule',
            name='time',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]