

from django.forms import ModelForm

from .models import masters

class mastersForm(ModelForm):
    class Meta:
        model = masters
        fields = ('UserLogin', 'cardNumber', 'accessLevel', 'rubric')