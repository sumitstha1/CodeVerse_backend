from django.urls import path
from .views import *

urlpatterns = [
    path("service/", ServiceApiView.as_view()),
    path("service/<slug>/", ServiceApiView.as_view()),
    path("blog/", BlogApiView.as_view()),
    path("blog/<slug>/", BlogApiView.as_view()),
]
