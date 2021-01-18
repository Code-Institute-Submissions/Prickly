from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings

from shopping_cart.contexts import cart_contents
from .forms import OrderForm

import stripe


def checkout(request):
    """ 
    A view that renders the checkout and connects
    cart contents to stripe
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # get cart contents. if empty, return an error msg
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty :(')
        return redirect(reverse('products'))

    # Get total of the cart as an integer
    cart_now = cart_contents(request)
    total = cart_now['total']
    stripe_total = round(total * 100)
    # Set the api key and create stripe intent with amount and currency
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
