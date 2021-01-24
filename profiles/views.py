from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from memberships.models import Membership
from .models import Profile
from .forms import ProfileForm


def profile(request):
    """ A view to return the profile page """
    profile = get_object_or_404(Profile, user=request.user)
    membership = get_object_or_404(Membership, name=profile.membership)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Well done you! Your '
                                      'details were updated :)')
        else:
            messages.error(request, 'Uh oh, something went wrong. '
                                    'Try again and make sure all '
                                    'fields are valid!')
    else:
        profile_form = ProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'membership': membership,
        'profile_form': profile_form,
        'on_profile': True,
    }

    return render(request, template, context)
