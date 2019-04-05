from django.shortcuts import render
from .models import Leaderboard
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):

	return render(request, 'leaderboard/leaderboard_list.html')
# Create your views here.

class LeaderboardListView(ListView):
    model = Leaderboard
    context_object_name = 'leaderboard'

    template_name = 'leaderboard/leaderboard_list.html'

class LeaderboardCreateView(CreateView):
    model = Leaderboard    
    fields = ['sport', 'team', 'win', 'lose', 'rank' ]

class LeaderboardUpdateView(UpdateView):
    model = Leaderboard
    fields = ['sport', 'team', 'win', 'lose', 'rank' ]

    def form_valid(self, form):
        print("VALID")
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_valid(form)

class LeaderboardDeleteView(DeleteView):
    model = Leaderboard
    success_url = '/leaderboard'
    