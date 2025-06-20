from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:index')
    
    else:
        form = ContactForm()
    
    return render(request, 'contact/create.html', {'form': form})

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact:contact', contact_id=contact.id)
    
    else:
        form = ContactForm(instance=contact)
    
    return render(request, 'contact/update.html', {'form': form})

def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact:index')
    
    return render(request, 'contact/delete.html', {'contact': contact})