from django.shortcuts import render
from .models import Review


def reviews(request):
    reviews = Review.objects.all()
    template = 'reviews/includes/reviews.html'
    context = {
        'reviews': reviews,
    }
    return render(request, template, context)
