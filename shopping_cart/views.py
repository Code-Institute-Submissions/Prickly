from django.shortcuts import render, redirect, reverse


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
    qty = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Check if product is already in the cart
    if product_id in list(cart.keys()):
        # If in the cart, increase quantity
        cart[product_id] += qty
    else:
        # Add to the cart if not in it already
        cart[product_id] = qty

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

