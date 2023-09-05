from django.shortcuts import render
from .models import Thickness

def index(request):

    its = Thickness.objects.all()
    context = {'its': its}
    return render(request, 'thickness/index.html', context)
