



from django.urls import path

from changestory.views import index



app_name = 'changestory'
urlpatterns = [
    path('', index, name='index'),

]
