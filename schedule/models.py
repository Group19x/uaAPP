from django.db import models
from django.urls import reverse
'''
Schedule Database

Table Name: Schedule
Table Attributes: teamOne, teamTwo, venue, date, time

Has three entries:
UP vs. Ateneo
AdU vs. UST
DLSU vs. FEU
'''

class Schedule(models.Model):
    teamOne = models.CharField(max_length = 100)
    teamTwo = models.CharField(max_length = 100)
    venue = models.CharField(max_length = 100)
    date = models.CharField(max_length = 100)
    time = models.CharField(max_length = 100)

    def __str__(self):
        return self.teamOne + "-" + self.teamTwo

    def get_absolute_url(self):
    	return reverse('post-detail', kwargs={'pk': self.pk})