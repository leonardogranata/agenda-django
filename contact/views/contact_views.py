from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from django.http import Http404 
from django.core.paginator import Paginator

def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')
    paginator = Paginator(contacts, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'contact/index.html', {'page_obj': page_obj, 'site_title': 'Contatos - '})

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects\
    .filter(show=True)\
    .filter(
        Q(firstName__icontains=search_value) |
        Q(lastName__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value) 
        )\
        .order_by('-id')
    
    paginator = Paginator(contacts, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'contact/index.html', {'page_obj': page_obj, 'site_title': 'Contatos - ', 'search_value': search_value})


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact.objects, pk=contact_id, show=True)
    site_title = f'{single_contact.firstName} {single_contact.lastName} - '

    return render(request, 'contact/contact.html', {'contact': single_contact, 'site_title': site_title})

