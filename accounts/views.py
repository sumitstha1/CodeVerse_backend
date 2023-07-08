from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *



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
    
class AboutApiView(APIView):
    def get(self, request):
        about_obj = About.objects.all()
        serializer = AboutSerializer(about_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class OurValueApiView(APIView):
    def get(self, request):
        our_value_obj = OurValue.objects.all().order_by("order")
        serializer = OurValueSerializer(our_value_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)