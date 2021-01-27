from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import ReviewForm
from products.models import Product
from profiles.models import Profile


def add_review(request, product_id):
    """
    Allow user to add a review and redirect them back to the
    item product item view
    """
    # Get current user and product
    user = Profile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    # Initiate review form
    review_form = ReviewForm()
    # Get details submitted by the user
    review_details = {
        'title': request.POST['title'],
        'description': request.POST['description'],
        'rating': request.POST['rating'],
    }
    # Add details to the form
    review_form = ReviewForm(review_details)

    # If form is valid, add user and product and save
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = user
        review.product = product
        review.save()
        # Success message if added
        messages.success(request, 'Thanks! Your review was added :)')
    else:
        # Error message if form was invalid
        messages.error(request, 'Uh oh, something went wrong. '
                                'Make sure the form is valid.')

    return redirect(reverse('product_item', args=(product_id,)))
