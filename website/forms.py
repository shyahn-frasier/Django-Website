from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'number', 'email', 'message')

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        phone = cleaned_data.get('number')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not phone and not email and not message:
            raise forms.ValidationError('You have to write something!')
