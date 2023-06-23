from rest_framework import serializers
from .models import *
from services.models import Service

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            "name",
            "email",
            "message"
        ]
        model = Contact

class HireSerializer(serializers.ModelSerializer):

    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())

    class Meta:
        fields = [
            "name",
            "company",
            "contact",
            "email",
            "service",
        ]
        model = Hire