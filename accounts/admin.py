from django.contrib import admin
from django.contrib.admin import register
from .models import *

# Register your models here.
@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "contact", "contact2"]

@register(SocialHandles)
class SocialHandlesAdmin(admin.ModelAdmin):
    pass

@register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    pass