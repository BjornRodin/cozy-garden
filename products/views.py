from django.shortcuts import render, get_object_or_404
from .models import Flowers


def all_products(request):
    """ Showing all flowers, and will include sorting and search queries later """

    products = Flowers.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Render the specific product detail page for the product the user has clicked """

    product = get_object_or_404(Flowers, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
