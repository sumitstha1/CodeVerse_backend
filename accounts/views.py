from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
class ProfileApiView(APIView):
    def get_obj(self, slug):
        try:
            return Profile.objects.get(slug = slug)
        except Profile.DoesNotExist:
            return None
        
    def get(self, request, slug = None):
        if slug:
            profile_obj = self.get_obj(slug)
            if not profile_obj:
                return Response({"error": "Profile with that slug not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = ProfileSerializer(profile_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        profile_obj = Profile.objects.all()
        serializer = ProfileSerializer(profile_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class NewsletterApiView(APIView):
    def post(self, request):
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)