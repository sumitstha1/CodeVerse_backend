from django.contrib import admin
from django.contrib.admin import register
from .models import *

# Register your models here.
@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "contact", "contact2"]

@register(SocialHandles)
class SocialHandlesAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]

@register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["email"]

@register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["slug"]

@register(OurValue)
class OurValueAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "order"]
    ordering = ["order"]

@register(Portfolio)
class OurValueAdmin(admin.ModelAdmin):
    list_display = ["title"]
    ordering = ["updated_at"]

@register(Testimonial)
class OurValueAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["updated_at"]