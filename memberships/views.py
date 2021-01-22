from django.shortcuts import render


def memberships(request):
    """ A view to return the memberships page """
    return render(request, 'memberships/memberships.html')
