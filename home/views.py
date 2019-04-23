from django.shortcuts import render
from users.models import Registered_User

from django.views.generic import View
from django.shortcuts import render

'''
Passes to home/main.html the username of the current registered user and his type contained in the table Registered_users
'''


def main(request):
    return render(request, 'home/main.html')

