from django.db import models
from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from .forms import ContactForm
from django.http import JsonResponse
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', {'contacts': contacts})

def search(request,q):
    contacts = Contact.objects.filter(
        models.Q(first_name__icontains=q) | models.Q(last_name__icontains=q)
    )
    # Utilisez le sérialiseur pour sérialiser les données
    serializer = ContactSerializer(contacts, many=True)
    serialized_data = serializer.data

    # Renvoyez les données sérialisées en tant que réponse JSON
    return JsonResponse({'contacts': serialized_data})


def contact_show(request,pk):
    contacts = Contact.objects.all()
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contacts/show.html', {'contact': contact,'contacts':contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        contacts = Contact.objects.all()
        form = ContactForm()
    return render(request, 'contacts/create.html', {'form': form,'contacts': contacts})

def contact_update(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm(instance=contact)
        contacts = Contact.objects.all()
    return render(request, 'contacts/create.html', {'form': form,'contacts': contacts})

def contact_delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('index')