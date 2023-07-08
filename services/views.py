from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
class ServiceApiView(APIView):
    def get_obj(self, slug):
        try:
            return Service.objects.prefetch_related("meta").order_by("order").get(slug = slug)
        except Service.DoesNotExist:
            return None
        
    def get(self, request, slug = None):
        if slug:
            service_obj = self.get_obj(slug)
            if not service_obj:
                return Response({"error": "Service with the slug not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = ServiceSerializer(service_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        service_obj = Service.objects.prefetch_related("meta").order_by("order").all()
        serializer = ServiceSerializer(service_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BlogApiView(APIView):
    def get_obj(self, slug):
        try:
            return Blog.objects.prefetch_related("section", "meta").get(slug = slug)
        except Blog.DoesNotExist:
            return None
        
    def get(self, request, slug=None):
        if slug:
            blog_obj = self.get_obj(slug)
            if not blog_obj:
                return Response({"error": "no such blog with that slug"}, status=status.HTTP_404_NOT_FOUND)
            serializer = BlogSerializer(blog_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        blog_obj = Blog.objects.prefetch_related("meta").all()
        serializer = BlogSerializer(blog_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)