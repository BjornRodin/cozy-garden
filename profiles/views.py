from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, FavoriteList
from .forms import UserProfileForm
from products.models import Flowers
from checkout.models import Order


@login_required
def profile(request):
    """ Display the profile for user """
    profile = get_object_or_404(UserProfile, user=request.user)

    try:
        favoritelist = FavoriteList.objects.get(user=request.user)
    except FavoriteList.DoesNotExist:
        favoritelist = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully \
                updated!')
        else:
            messages.error(request, 'Update failed. Please make sure \
                the form is valid and try again.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'favoritelist': favoritelist,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a old confirmation for order {order_number}. '
        'A confirmation email was sent when the order was made.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_favorite(request, product_id):
    """ Add product to favorites """
    product = get_object_or_404(Flowers, id=product_id)
    favoritelist, created = FavoriteList.objects.get_or_create(user=request.user)

    if product not in favoritelist.products.all():
        favoritelist.products.add(product)
        messages.success(request, f'{product.name} added to favorites!')
    else:
        messages.info(request, f'{product.name} is already a favorite.')

    return redirect('product_detail', product_id=product_id)