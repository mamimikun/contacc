from django.shortcuts import render
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.decorators import api_view
from django.core.paginator import Paginator


# Create your views here 

@api_view(['GET'])
def contactList(request):
    contacts = Contact.objects.all()
    paged = Paginator(contacts, 3)
    page_num = request.GET.get('page')
    page_obj = paged.get_page(page_num)
    
    # serializer = ContactSerializer(contacts, many=True)
    
    # return render
    return render(request, 'contaccs/contact_list.html', {'page_obj': page_obj})

@api_view(['GET'])
def contactRead(request, contact_id):
    contacts = Contact.objects.get(id=contact_id)
    serializer = ContactSerializer(contacts, many=False)
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
def contactUpdate(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    serializer = ContactSerializer(instance=contact, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])
def contactDelete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return Response('deleted')
