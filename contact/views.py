from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    """ Renders the contact page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/contact_success.html')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
