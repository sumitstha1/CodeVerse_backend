from django.contrib import admin
from django.contrib.admin import register
from .models import *

# Register your models here.
class BlogMetaInline(admin.StackedInline):
    model = BlogMetaTags

class ServiceMetaInline(admin.StackedInline):
    model = ServiceMetaTags

@register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceMetaInline]
    list_display = ["title", "slug", "order"]
    ordering = ["order"]

@register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = (BlogMetaInline,)
    # pass

@register(BlogSection)
class BlogSectionAdmin(admin.ModelAdmin):
   list_display = ["blog", "order"]
   ordering = ['order']