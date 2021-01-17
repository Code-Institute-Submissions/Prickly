from django.shortcuts import render


def checkout(request):
    """ A view that renders the checkout """

    return render(request, 'checkout/checkout.html')
