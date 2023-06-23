from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from services.models import Service

# Create your views here.
class ContactApiView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
class HireApiView(APIView):
    def post(self, request):
        try:
            service_uid = request.data.get('service')
            service = Service.objects.get(uid = service_uid)
            data = {
                'name': request.data.get('name'),
                'company': request.data.get('company'),
                'email': request.data.get('email'),
                'contact': request.data.get('contact'),
                'service': service.uid,
            }
            serializer = HireSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Service.DoesNotExist:
            return Response({"error": "no such service found"})