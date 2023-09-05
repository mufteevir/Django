



from django.urls import path

from bboard.views import index, by_rubric
from .views import mastersCreateView

app_name = 'bboard'
urlpatterns = [
    path('add/', mastersCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]
