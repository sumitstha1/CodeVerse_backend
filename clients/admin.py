from django.contrib import admin
from django.contrib.admin import register
from .models import *

# Register your models here.
@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@register(Hire)
class HireAdmin(admin.ModelAdmin):
    pass