from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Flowers


def all_products(request):
    """ Showing all flowers, and will include sorting and search queries later """

    products = Flowers.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You need to enter a search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(instructions__icontains=query) | Q(color__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Render the specific product detail page for the product the user has clicked """

    product = get_object_or_404(Flowers, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
