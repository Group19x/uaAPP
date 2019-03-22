from django.db import models
from django.urls import reverse
'''
Leaderboard Database

Table Name: Leaderboard
Table Attributes: Sport, Team, Win, Lose, Rank


'''

class Leaderboard(models.Model):
    id = models.AutoField(primary_key=True)
    sport = models.CharField(max_length = 100)
    team = models.CharField(max_length = 100)
    win = models.IntegerField()
    lose = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return self.sport

    def get_absolute_url(self):
    	return reverse('leaderboard')
