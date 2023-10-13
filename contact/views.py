from django.shortcuts import render
from django.http import HttpResponse


def contact_us(request):
    """ Renders the contact page """

    
    return HttpResponse("Contact app works!")
