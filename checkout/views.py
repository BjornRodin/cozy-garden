from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your cart is empty at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Nx6ZLEwXoLWvCjTQ2NY0lqan93Wj7UE1sYwUttGJIG4lzhs1dccUh4sbVGaVFAiEkcLG4iMsqfQP7sNcGEh0DOP009dpqJqmX',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)