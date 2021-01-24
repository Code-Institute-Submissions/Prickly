from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Membership
from profiles.models import Profile
from django.contrib import messages


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
    # Save chosen membership in user profile
    if request.method == 'POST':
        try:
            user_membership_value = request.POST.get('user-membership')
            user_membership = get_object_or_404(
                Membership, name=user_membership_value)
            profile = get_object_or_404(Profile, user=request.user)
            profile.membership = user_membership
            profile.save()
            # Display confirmation
            messages.success(request, 'Congrats!! You successfully subscribed '
                                      f'to the {user_membership} membership!')
            # Redirect the user to profiles page
            return redirect(reverse('profile'))
        # If there was an issue with attaching membership to the profile
        except (KeyError, NameError):
            # Display an error message
            messages.error(request, 'Something went wrong')
            # Redirect back to the membership_checkout page
            return redirect(reverse('membership_checkout'))

    # Retrieve data for all memberships
    all_memberships = Membership.objects.all()

    # If user is updating selected membership, the
    # memberhip_type to the new vlue
    if request.GET.get('membership-new'):
        membership_type = request.GET.get('membership-new')

    # If user logged in after
    # registering, get membership_type from session
    else:
        try:
            # Retrieve user selected membership
            membership_type = request.session['membership']
        except KeyError:
            # If user logged in normally, redirect them
            # to the profile page
            return redirect(reverse('products'))

    # Retrieve data for selected membership type
    membership = get_object_or_404(Membership, name=membership_type)

    template = 'memberships/membership_checkout.html'
    context = {
        'membership': membership,
        'all_memberships': all_memberships,
    }

    return render(request, template, context)
