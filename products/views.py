from django.shortcuts import render


def all_products(request):
    """Return a page with all products displayed"""
    return render(request, 'products/products.html')
