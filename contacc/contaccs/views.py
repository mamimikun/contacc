from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import redirect
from .models import Contact
from .forms import ContactForm
from .serializers import ContactSerializer
from rest_framework.decorators import api_view
from django.core.paginator import Paginator


# Create your views here 

@api_view(['GET'])
def contactList(request):
    contacts = Contact.objects.all()
    paged = Paginator(contacts, 10)
    page_num = request.GET.get('page')
    page_obj = paged.get_page(page_num)

    # serializer = ContactSerializer(contacts, many=True)
    
    # return render
    return render(request, 'contaccs/contact_list.html', {'page_obj': page_obj})

@api_view(['GET'])
def contactRead(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    serializer = ContactSerializer(contact, many=False)
    print(serializer.data)
    return render(request, 'contaccs/read.html', {'contact':serializer.data})
    #return Response(serializer.data)

# this pulls out the form
def contactCreate(request):
    action = '/api/contacts/create/'
    form = ContactForm()
    return render(request, 'contaccs/form.html',  {'form': form, 'action':action})

# the actual post verb
@api_view(['POST'])
def contactCreatePOST(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    response = redirect('/api/contacts/')
    return response

# same for update. first, pull out the form
def contactUpdate(request, contact_id):
    action = '/api/contacts/update/'+contact_id+'/'
    contact = Contact.objects.get(id=contact_id)
    form = ContactForm(instance=contact)
    return render(request, 'contaccs/form.html', {'form': form, 'action': action})
    
@api_view(['POST'])
def contactUpdatePOST(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    serializer = ContactSerializer(instance=contact, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    response = redirect('/api/contacts/')
    return response

@api_view(['GET'])
def contactDelete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    serializer = ContactSerializer(contact, many=False)
    contact.delete()
    return render(request, 'contaccs/delete.html', {'contact':serializer.data})
