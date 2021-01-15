from django.shortcuts import render


def cart(request):
    """ A view that renders the shopping_cart """

    return render(request, 'shopping_cart/cart.html')
