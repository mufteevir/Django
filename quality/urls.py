from django.urls import path

from quality.views import index



app_name = 'quality'
urlpatterns = [
    path('', index, name='index'),

]
