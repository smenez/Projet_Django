from django.db import models
from django.contrib.auth.models import User

class Inscription(models.Model) :
    pseudo = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    
class ToDoUserProfile(models.Model) :
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    
    pseudo = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)