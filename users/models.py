from django.db import models
from django.contrib.auth.models import User

class Registered_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices = (('team', 'Team'), ('admin', 'Admin')))

    def __str__(self):
        return self.user.get_username()