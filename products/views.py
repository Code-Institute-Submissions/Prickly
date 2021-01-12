from django.shortcuts import render

from .models import Product, Category, Color


def all_products(request):
    """
    Return a page with all products displayed
    """
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
