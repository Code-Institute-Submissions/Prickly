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


def membership_checkout(request):
    """
    Retrieve user selected membership, display it and
    benefits, and allow user to change the membership
    type
    """
    # Retrieve data for all memberships
    all_memberships = Membership.objects.all()

    # If user is updating selected membership, the
    # memberhip_type to the new vlue
    if request.GET.get('membership-new'):
        membership_type = request.GET.get('membership-new')

    # Otherwise get membership_type from session
    else:
        # Retrieve user selected membership
        membership_type = request.session['membership']

    # Retrieve data for selected membership type
    membership = get_object_or_404(Membership, name=membership_type)

    template = 'memberships/membership_checkout.html'
    context = {
        'membership': membership,
        'all_memberships': all_memberships,
    }

    return render(request, template, context)
