from django.shortcuts import render, get_object_or_404

from .models import Product, Category, Color


def all_products(request):
    """
    Return a page with all products displayed,
    Allow user to select category and filter objects by it
    Allow user to sort items
    """
    products = Product.objects.all()
    categories = Category.objects.all()
    item_category = 'All'

    # Filter objects by the selected category and save selected category
    if request.GET:
        if 'category' in request.GET:
            item_category = request.GET['category']
            products = products.filter(category__name=item_category)
            # Sorting functionality for all items and each category
            if 'sort' in request.GET:
                sort_by = request.GET['sort']
                if item_category == 'All':
                    products = Product.objects.order_by(sort_by)

                products = products.order_by(sort_by)

    context = {
        'products': products,
        'categories': categories,
        'active_category': item_category,
    }

    return render(request, 'products/products.html', context)


def product_item(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    colors = Color.objects.filter(product=product.pk)
    template = 'products/product_item.html'
    context = {
        'product': product,
        'colors': colors,
    }
    return render(request, template, context)
