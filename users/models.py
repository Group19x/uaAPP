from django.db import models
from django.contrib.auth.models import User

'''
Purpose: A model that allows the registered User to be assigned as a Team or Admin

Table Name: Registered_user
Table Attributes: user, type
'''

class Registered_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices = (('team', 'Team'), ('admin', 'Admin')))

    def __str__(self):
        return self.user.get_username()