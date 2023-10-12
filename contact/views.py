from django.shortcuts import render
from .forms import ContactForm


def contact_us(request):
    """ Renders the contact page """

    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
