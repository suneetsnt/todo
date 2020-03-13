from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):

    class  Meta:
        model = Task
        fields = '__all__'

class CartForm(forms.ModelForm):

    class  Meta:
        model = Cart
        fields = '__all__'

