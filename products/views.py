from django.shortcuts import render
from .models import Flowers


def all_products(request):
    """ Showing all flowers, and will include sorting and search queries later """

    products = Flowers.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
