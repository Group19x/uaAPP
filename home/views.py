from django.shortcuts import render
from users.models import Registered_User

'''
Passes to home/main.html the username of the current registered user and his type contained in the table Registered_users
'''


def main(request):

    username = request.user.get_username()
    type = "none"
    for e in Registered_User.objects.all():
        if e.__str__() == username:
            type = e.type
    return render(request, 'home/main.html', {'username':username, 'type':type})