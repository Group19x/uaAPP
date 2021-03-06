from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Schedule
from .forms import SchedCreateForm

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
	ordering = ['-id']

class SchedPostDetailView(DetailView):
	model = Schedule

def SchedPostCreateView(request):
	if request.method == 'POST':
	    form = SchedCreateForm(request.POST, request.FILES)
	    if form.is_valid():
	        form.save()
	        #form.save()
	        return HttpResponseRedirect('/')
	else:
	    form = SchedCreateForm()
	return render(request, 'news_create/news_create.html', {'form':form})


class SchedPostUpdateView(LoginRequiredMixin, UpdateView):
	model = Schedule	
	fields = ['teamOne', 'teamTwo', 'venue', 'date', 'time']

class SchedPostDeleteView(LoginRequiredMixin, DeleteView):
	model = Schedule
	success_url = '/schedule'