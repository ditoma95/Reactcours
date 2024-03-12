from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
class ContactDetail(generics.RetrieveAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
class ContactUpdate(generics.UpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    def perform_update(self, serializer):
        avatar_file = self.request.data.get('avatar')
        serializer.save(avatar=avatar_file)
class ContactDelete(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer