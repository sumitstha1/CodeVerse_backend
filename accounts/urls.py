from django.urls import path
from .views import *

urlpatterns = [
    path("profile/", ProfileApiView.as_view()),
    path("profile/<slug>/", ProfileApiView.as_view()),
    path("newsletter/", NewsletterApiView.as_view()),
]
