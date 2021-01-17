from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def cart(request):
    """ A view that renders the shopping_cart """

    return render(request, 'shopping_cart/cart.html')


def add_item_to_cart(request, product_id):
    """
    Start a cart session item,
    Add product details and quantity to the cart,
    Redirect user back to the url they were at
    """
    # get cart session if avaialble, initiate otherwise
    product = get_object_or_404(Product, pk=product_id)
    qty = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Check if product is already in the cart
    if product_id in list(cart.keys()):
        # If in the cart, increase quantity
        cart[product_id] += qty
        messages.warning(request, f'Added more of "{product.name}".')
    else:
        # Add to the cart if not in it already
        cart[product_id] = qty
        messages.warning(request, f'Added "{product.name}" to the cart.')

    # assign values to cart
    request.session['cart'] = cart
    return redirect(redirect_url)


def change_cart(request, product_id):
    """
    Handle changes made in the cart
    Update the quantity if changed
    If quantity is 0, remove the item
    """
    qty = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    # If quantity is bigger than 0, change it, otherwise remove item
    if qty > 0:
        cart[product_id] = qty
    else:
        cart.pop(product_id)

    # assign values to cart
    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_item_from_cart(request, product_id):
    """
    Remove seleced item from the cart,
    Try to remove a selected item from cart and return
    successful status code 200 of item was successfully
    removed
    Otherwise return internal server error status code 500
    """

    try:
        cart = request.session.get('cart', {})
        # Remove item from the session cart
        cart.pop(product_id)

        # re-assign values to cart
        request.session['cart'] = cart
        # return successful status code
        return HttpResponse(status=200)
    except Exception as e:
        # return internal server error status code
        return HttpResponse(status=500)
        print(e)
