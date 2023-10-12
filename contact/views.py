from django.shortcuts import render


def contact_us(request):
    """ Renders the contact page """
    return render(request, 'contact/contact.html')
