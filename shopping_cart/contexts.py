

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
