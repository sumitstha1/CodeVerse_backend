from rest_framework import serializers
from .models import *

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Service

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Blog

class BlogSectionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = BlogSection