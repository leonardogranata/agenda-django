from django.shortcuts import render
from contact.models import Contact

def index(request):
    contacts = Contact.objects\
    .filter(show=True)\
    .order_by('-id')
    return render(request, 'contact/index.html', {'contacts': contacts})


