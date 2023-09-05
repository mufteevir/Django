from django.contrib import admin

from django.contrib import admin
from .models import masters
from django . contrib import admin
from .models import Rubric

class mastersAdmin(admin.ModelAdmin):
    list_display = ('UserLogin', 'accessLevel', 'cardNumber', 'published', 'rubric')
    list_display_links = ('UserLogin', 'cardNumber')
    search_fields = ('UserLogin', 'cardNumber',)
admin.site.register(masters, mastersAdmin)
admin.site.register(Rubric)
