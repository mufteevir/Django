from django.shortcuts import render

from django.http import HttpResponse
from .models import masters
from .models import Rubric
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import mastersForm
from django.urls import reverse_lazy


def index(request):

    mms = masters.objects.all()
    rubrics = Rubric.objects.all()
    context = {'mms': mms, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):

    mms = masters.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'mms': mms, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class mastersCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = mastersForm
    success_url = reverse_lazy('bboard:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

