from django import forms
from django.contrib.auth.models import User
from schedule.models import Schedule

class SchedCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['teamOne', 'teamTwo', 'venue', 'date', 'time',]
    #image = forms.ImageField()
    #title = forms.CharField(max_length=100)
    #author = forms.CharField(max_length=100)
    #body = forms.CharField()
    #date_and_time = forms.DateTimeField()