from django.db import models
from django.urls import reverse
'''
Leaderboard Database

Table Name: Leaderboard
Table Attributes: Sport, Team, Win, Lose, Rank


'''

class Leaderboard(models.Model):
    id = models.AutoField(primary_key=True)
    sport = models.CharField(max_length = 100, verbose_name='Sport')
    team = models.CharField(max_length = 100, verbose_name='Team')
    win = models.IntegerField(verbose_name='Win')
    lose = models.IntegerField(verbose_name='Loss')
    rank = models.IntegerField(verbose_name='Rank')

    def __str__(self):
        return self.sport

    def get_absolute_url(self):
    	return reverse('leaderboard')

    class Meta:
        ordering = ['sport']