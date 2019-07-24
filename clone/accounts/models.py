from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):


    def str(self):
        return "@{}".format(self.username)
