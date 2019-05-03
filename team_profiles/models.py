from django.db import models
from django.urls import reverse
# Create your models here.
class Team_Profile(models.Model):
	teamName = models.CharField(max_length=100, verbose_name='Team Name')
	image = models.ImageField(upload_to='Images/%Y/%m/%d/', verbose_name='Image', blank = True)
	email = models.CharField(max_length=100, verbose_name='Email Adress')
	rec_email = models.CharField(max_length=100, verbose_name='Recovery Email')
	creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')

	def __str__(self):
		return self.teamName

	def get_absolute_url(self):
		return reverse('team-detail', kwargs={'pk': self.pk}) 

class Player_Profile(models.Model):
	teamID = models.ForeignKey(Team_Profile, null = True, on_delete=models.CASCADE, verbose_name='Team Name')
	player_name = models.CharField(max_length=100, verbose_name='Player Name')
	sports = models.CharField(max_length=100, verbose_name='Sport')
	year_level = models.IntegerField(verbose_name='Year Level')
	position = models.CharField(max_length=100, verbose_name='Position')

	def __str__(self):
		return self.player_name

	class Meta:
		ordering = ['sports']
