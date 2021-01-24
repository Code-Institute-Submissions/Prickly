from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def membership_type(request):
    """
    Capture membership type selected by user, store it in
    session variable and redirect user to the signup page
    """

    membership_type = request.POST.get('membership_type')
    request.session['membership'] = membership_type

    return redirect(reverse('account_signup'))
