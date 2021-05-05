from django.shortcuts import render
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def contactList(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def contactCreate(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)

@api_view(['POST'])
def contactUpdate(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)
