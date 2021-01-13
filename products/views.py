from django.shortcuts import render

from .models import Product, Category, Color


def all_products(request):
    """
    Return a page with all products displayed,
    Allow user to select category and filter objects by it
    """
    products = Product.objects.all()
    categories = Category.objects.all()
    item_category = 'All'

    # Filter objects by the selected category and save selected category
    if request.GET:
        if 'category' in request.GET:
            item_category = request.GET['category']
            products = products.filter(category__name=item_category)

    context = {
        'products': products,
        'categories': categories,
        'active_category': item_category,
    }

    return render(request, 'products/products.html', context)
