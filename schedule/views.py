from django.shortcuts import render
from django.http import HttpResponse
from .models import Schedule

'''
Passes to schedule/sched.html the table Schedule on models.py
'''

def Posts(request):
	context = {
		'sched' : Schedule.objects.all()
	}
	return render(request, 'schedule/sched.html', context) 