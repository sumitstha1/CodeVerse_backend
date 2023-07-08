from rest_framework import serializers
from .models import *

class ServiceMetaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = ServiceMetaTags

class BlogMetaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = BlogMetaTags

class ServiceSerializer(serializers.ModelSerializer):

    meta = ServiceMetaSerializer()

    class Meta:
        fields = "__all__"
        model = Service

class BlogSectionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = BlogSection

class BlogSerializer(serializers.ModelSerializer):

    section = BlogSectionSerializer(many=True)
    meta = BlogMetaSerializer()

    class Meta:
        fields = "__all__"
        model = Blog
