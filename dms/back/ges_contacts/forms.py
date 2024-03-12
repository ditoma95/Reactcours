from django import forms
from contacts.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'phone': 'Téléphone',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded'}),
            'phone': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded'}),
        }
