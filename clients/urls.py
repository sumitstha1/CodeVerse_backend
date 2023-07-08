from django.urls import path
from .views import *

urlpatterns = [
    path("contact/", ContactApiView.as_view()),
    path("hire/", HireApiView.as_view()),
]
