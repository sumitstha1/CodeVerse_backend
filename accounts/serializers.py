from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Profile

class SocialHandlesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = SocialHandles

class NewsletterSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            "email"
        ]
        model = Newsletter

class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = About

class OurValueSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = OurValue