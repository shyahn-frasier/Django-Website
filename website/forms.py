from django import forms
from .models import Name, Phone_Number, Message

#class NameForm(forms.Form):
  #  class Meta:
      #  model = Name
      #  fields = ('text',)

#class PhoneNumberForm(forms.ModelForm):
  # class Meta:
     #   model = Phone_Number
     #   fields = ('text',)

#class MessageForm(forms.ModelForm):
    #class Meta:
      #  model = Message
       # fields = ('text',)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=250)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write your message here!'
    )
    source = forms.CharField(max_length=50, widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')
