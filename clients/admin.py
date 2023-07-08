from django.contrib import admin
from django.contrib.admin import register
from .models import *

# Register your models here.
@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "is_read", "created_at"]
    list_filter = ["is_read", "created_at"]

@register(Hire)
class HireAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "contact", "email", "service", "is_read", "is_accept", "created_at"]
    list_filter = ["is_read", "is_accept", "created_at"]