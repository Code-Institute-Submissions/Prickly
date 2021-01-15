from decimal import Decimal
from django.conf import settings


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

    grand_total = total + delivery_cost

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery_type': delivery_type,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }

    return context
