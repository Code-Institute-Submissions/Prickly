from django.shortcuts import render
from .models import Membership


def memberships(request):
    """
    A view to return the memberships page
    """

    # Get all membership model entries
    memberships = Membership.objects.all()
    template = 'memberships/memberships.html'
    context = {
        'memberships': memberships,
    }
    return render(request, template, context)
