from django.shortcuts import render
from .models import Presentations

def index(request):

    its = Presentations.objects.all()
    context = {'its': its}
    return render(request, 'changestory/index.html', context)