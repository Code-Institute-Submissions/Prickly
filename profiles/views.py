from django.shortcuts import render, get_object_or_404
from memberships.models import Membership
from .models import Profile
from .forms import ProfileForm


def profile(request):
    """ A view to return the profile page """
    profile = get_object_or_404(Profile, user=request.user)
    membership = get_object_or_404(Membership, name=profile.membership)
    profile_form = ProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'membership': membership,
        'profile_form': profile_form,
    }

    return render(request, template, context)
