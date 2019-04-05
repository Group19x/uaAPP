# Generated by Django 2.1.5 on 2019-04-05 04:52

from django.db import migrations, models
import django.utils.timezone
import schedule.models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_auto_20190405_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date_and_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, validators=[schedule.models.validate_date]),
        ),
    ]