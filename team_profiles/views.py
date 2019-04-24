from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Team_Profile, Player_Profile

class TeamListView(ListView):
	model = Team_Profile
	template_name = 'team_profiles/teams.html'
	context_object_name = 'teams'
	ordering = ['teamName']

class TeamDetailView(DetailView):
	model = Team_Profile
	context_object_name = 'teams'

class TeamCreateView(CreateView):
	model = Team_Profile
	fields = ['teamName', 'email', 'rec_email']

class TeamUpdateView(UpdateView):
	model = Team_Profile
	fields = ['teamName', 'email', 'rec_email']

class TeamDeleteView(DeleteView):
	model = Team_Profile
	success_url = '/team_profiles'

class PlayerCreateView(CreateView):
	model = Player_Profile
	fields = ['teamID', 'player_name', 'sports', 'year_level', 'position']
	success_url = '/team_profiles'

class PlayerDeleteView(DeleteView):
	model = Player_Profile
	success_url = '/team_profiles'