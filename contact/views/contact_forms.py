from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from contact.forms import ContactForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='contact:login')
def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:index')
    else:
        form = ContactForm()
    
    return render(request, 'contact/create.html', {'form': form})

@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            if form.cleaned_data.get('remove_picture'):
                contact.picture.delete(save=False)
                contact.picture = None
            form.save()
            return redirect('contact:contact', contact_id=contact.id)
    else:
        form = ContactForm(instance=contact)
    
    return render(request, 'contact/update.html', {'form': form})

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, owner=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact:index')
    
    return render(request, 'contact/delete.html', {'contact': contact})
