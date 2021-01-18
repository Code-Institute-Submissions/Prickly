from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from shopping_cart.contexts import cart_contents
from .forms import OrderForm
from products.models import Product
from .models import OrderLine

import stripe


def checkout(request):
    """
    A view that renders the checkout and saves the data user has
    put into the order info form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Get data out of the submitted form
        cart = request.session.get('cart', {})
        order_info = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'city': request.POST['city'],
            'region': request.POST['region'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'delivery_type': request.POST['delivery_type']
        }
        # Save the data in Order Form if valid
        order_form = OrderForm(order_info)
        if order_form.is_valid():
            order = order_form.save()
            order_form.save()
            for product_id, qty in cart.items():
                # Loop through items in the cart and add an instance of each
                # to the OrderLine model
                try:
                    product = Product.objects.get(id=product_id)
                    order_line = OrderLine(
                        order=order,
                        product=product,
                        quantity=qty,
                    )
                    order_line.save()
                except Product.DoesNotExist:
                    # Display an error message if something goes wrong
                    messages.error(request, (
                        "There was an issue with an item in your cart. "
                        "Try again later or contact us for assistance!")
                    )
                    # Delete the order and redirect back to the cart
                    order.delete()
                    return redirect(reverse('cart'))

            # Navigate user to the success checkout page
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            # If form is not valid, display an error message
            messages.error(request, 'There was an error with your form.'
                                    'Please double check your information.')
    else:
        # If request not POST, get cart contents. if empty, return an error msg
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'Your cart is empty :(')
            return redirect(reverse('products'))

        # Get total of the cart as an integer
        cart_now = cart_contents(request)
        print(cart_now)
        total = cart_now['grand_total']
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
