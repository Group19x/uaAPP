from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils import timezone
'''
Schedule Database

Table Name: Schedule
Table Attributes: teamOne, teamTwo, venue, date, time

Has three entries:
UP vs. Ateneo
AdU vs. UST
DLSU vs. FEU
'''

def validate_date(date):
    if date.date() < timezone.now().date():
        raise ValidationError("Date cannot be in the past")

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    teamOne = models.CharField(max_length = 100, verbose_name='Team One')
    teamTwo = models.CharField(max_length = 100, verbose_name='Team Two')
    sport = models.CharField(max_length = 100, blank = True, verbose_name='Sport')
    venue = models.CharField(max_length = 100, verbose_name='Venue')
    date_and_time = models.DateTimeField(default=timezone.now, blank = True, validators=[validate_date], verbose_name='Date and Time')
    image1 = models.ImageField(upload_to='Images/%Y/%m/%d/', blank = True, verbose_name='Team One Image')
    image2 = models.ImageField(upload_to='Images/%Y/%m/%d/', blank = True, verbose_name='Team Two Image')

    def __str__(self):
        return self.teamOne + "-" + self.teamTwo

    def get_absolute_url(self):
    	return reverse('post-detail', kwargs={'pk': self.pk})