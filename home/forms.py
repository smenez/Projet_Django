from . import models
from django import forms
from django.forms import ModelForm
from .models import Inscription

class FormulaireForm(ModelForm) :
    class Meta :
        model = Inscription
        fields = ('pseudo', 'email', 'password',)