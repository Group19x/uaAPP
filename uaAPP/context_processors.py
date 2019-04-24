from users.models import Registered_User

def current_user(request):
    username = request.user.get_username()
    type = "none"
    for e in Registered_User.objects.all():
        if e.__str__() == username:
            type = e.type
    return {'username':username, 'type':type}
