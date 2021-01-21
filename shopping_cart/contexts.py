from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Define a context dictionary cart_contents
    to be used accross all apps
    """
    cart_items = []
    total = 0
    item_count = 0
    delivery_type = None
    delivery_cost = 0
    discount = 0

    # retrieve cart session dictionary or initialize
    cart = request.session.get('cart', {})

    # Loop thorugh items in the cart
    for product_id, qty in cart.items():
        # Retrieve the product and get the quantity
        product = get_object_or_404(Product, pk=product_id)
        product_total = qty * product.price
        item_count += qty
        # Calculate total price of each type of items
        total += qty * product.price
        # Add these values to cart_items to be used globally
        cart_items.append({
            'product_id': product_id,
            'quantity': qty,
            'product': product,
            'product_total': product_total,
        })

    # Check the type of delivery and calculate delivery cost accordingly
    if delivery_type == 'standard':
        # Standard delivery is set under certain limit
        if total < settings.STANDARD_DELIVERY_LIMIT:
            delivery_cost = settings.STANDARD_DELIVERY_CONST

        # Delivery charge is a % on orders over the limit
        delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_RATE / 100)

    elif delivery_type == 'express':
        # Express delivery is set under certain limit
        if total < settings.EXPRESS_DELIVERY_LIMIT:
            delivery_cost = settings.EXPRESS_DELIVERY_CONST

        # Delivery charge is a % on orders over the limit
        delivery_cost = total * Decimal(settings.EXPRESS_DELIVERY_RATE / 100)

    # If user is eligble for a discount, calculate it here
    discount_price = total * Decimal(discount / 100)
    grand_total = round((total + delivery_cost - discount_price), 2)

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery_type': delivery_type,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
        'discount': discount,
    }

    return context
