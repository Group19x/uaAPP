from django.shortcuts import render
from users.models import Registered_User

def main(request):

    username = request.user.get_username()
    type = "none"
    for e in Registered_User.objects.all():
        if e.__str__() == username:
            type = e.type
    return render(request, 'home/main.html', {'username':username, 'type':type})