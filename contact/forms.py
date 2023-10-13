from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """ Setting up the contactform """
    class Meta:
        model = Contact
        fields = '__all__'
