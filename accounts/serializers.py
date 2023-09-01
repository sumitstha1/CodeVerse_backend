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

class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "image",
            "name",
            "role",
            "content"
        ]
        model = Testimonial

class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "image",
            "title",
            "link"
        ]
        model = Portfolio