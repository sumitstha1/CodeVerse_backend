from django.db import models
from base.models import BaseModel
from services.models import Service

# Create your models here.
class Contact(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    is_read = models.BooleanField(default=False)

class Hire(BaseModel):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255)
    email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="hire")
    is_read = models.BooleanField(default=False)
    is_accept = models.BooleanField(default=False)