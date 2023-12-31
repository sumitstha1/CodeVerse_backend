from django.urls import path
from .views import *

urlpatterns = [
    path("profile/", ProfileApiView.as_view()),
    path("profile/<slug>/", ProfileApiView.as_view()),
    path("newsletter/", NewsletterApiView.as_view()),
    path("about/", AboutApiView.as_view()),
    path("ourvalue/", OurValueApiView.as_view()),
    path("testimonial/", TestimonialApiView.as_view()),
    path("portfolio/", PortfolioApiView.as_view()),
]
