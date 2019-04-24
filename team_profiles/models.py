from django.db import models
from django.urls import reverse
# Create your models here.
class Team_Profile(models.Model):
	teamName = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	rec_email = models.CharField(max_length=100)
	creation_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.teamName

	def get_absolute_url(self):
		return reverse('team-detail', kwargs={'pk': self.pk}) 

class Player_Profile(models.Model):
	teamID = models.ForeignKey(Team_Profile, on_delete=models.CASCADE)
	player_name = models.CharField(max_length=100)
	sports = models.CharField(max_length=100)
	year_level = models.IntegerField()
	position = models.CharField(max_length=100)

	def __str__(self):
		return self.player_name
