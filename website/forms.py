from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div


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

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Field('name', css_class="form-group col-md-4 mb-0 form-contact-info"),
                Field('number', css_class="form-group col-md-4 mb-0 form-contact-info"),
                Field('email', css_class="form-group col-md-4 mb-0 form-contact-info"),
                Field('message', css_class="form-group form-contact-info")
        )
        #self.helper.form_class = 'form-contact-info'
        #self.helper.form_method = 'post'
