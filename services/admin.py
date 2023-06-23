from django.contrib import admin
from django.contrib.admin import register
from .models import *

# Register your models here.
@register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@register(BlogSection)
class BlogSectionAdmin(admin.ModelAdmin):
    pass