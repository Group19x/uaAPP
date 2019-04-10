from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Schedule

'''
Passes to schedule/sched.html the table Schedule on models.py
'''


def SchedPost(request):
    context = {
        'sched' : Schedule.objects.all()
    }
    return render(request, 'schedule/sched.html', context) 

class SchedPostListView(ListView):
    model = Schedule
    template_name = 'schedule/sched.html'
    context_object_name = 'sched'
    ordering = ['sport']

class SchedPostDetailView(DetailView):
    model = Schedule

class SchedPostCreateView(LoginRequiredMixin, CreateView):
    model = Schedule    
    fields = ['teamOne', 'teamTwo', 'sport', 'venue', 'date_and_time', 'image1', 'image2']

class SchedPostUpdateView(LoginRequiredMixin, UpdateView):
    model = Schedule	
    fields = ['teamOne', 'teamTwo', 'sport', 'venue', 'date_and_time', 'image1', 'image2']

class SchedPostDeleteView(LoginRequiredMixin, DeleteView):
    model = Schedule
    success_url = '/schedule'