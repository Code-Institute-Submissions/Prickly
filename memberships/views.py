import stripe

from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse

from .models import Membership, StripeCustomer
from profiles.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User


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


@login_required
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
        # add membership type to session to retrieve for stripe
        request.session['membership'] = membership_type

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


"""
The following code was taken from
https://testdriven.io/blog/django-stripe-subscriptions/
and
https://stripe.com/docs/billing/subscriptions/checkout
It is used to set up Stripe external checkout form
to handle subscriptions and was customized
"""


@csrf_exempt
def stripe_config(request):
    """
    Handles AJAX requests coming from stripe_sub.js
    """
    if request.method == 'GET':
        # add public key in a dict that will be retrieved by JS
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    """
    Creates the Checkout Session with product details
    and returns Checkout Session ID to be fetched by
    frontend
    """
    if request.method == 'GET':
        # define domain URL
        domain_url = settings.DOMAIN_URL
        # set stripe API from SECRET KEY variable
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # get user chosen membership from session
        membership = request.session['membership']
        # set stripe product price dependant on above
        if membership == 'Ultimate':
            price = settings.STRIPE_PRICE_ID_ULTIMATE
        else:
            price = settings.STRIPE_PRICE_ID_SUPREME
        try:
            # Create a Checkout Session
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=(request.user.id if
                                     request.user.is_authenticated else None),
                # link to checkout success page if paymenr successful
                success_url=(
                    domain_url + 'success?session_id={CHECKOUT_SESSION_ID}'),
                #  Link to a page if user cancels the payment in checkout
                cancel_url=domain_url + 'membership_checkout/',
                # Define payment method to be a card
                payment_method_types=['card'],
                # Subscription model
                mode='subscription',
                # Price and quantity of items
                line_items=[
                    {
                        'price': price,
                        'quantity': 1,
                    }
                ]
            )
            # Return Checkout Session ID
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def success(request):
    return render(request, 'memberships/sub_success.html')


@csrf_exempt
def stripe_webhook(request):
    """
    Create a new StripeCustomer every time someone subscribes
    to the membership by using Stripe Webhook
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WH_SECRET_SUB
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Return status 400 if payload is invalid
        messages.error(request, f'error: {e}')
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Return status 400 if signature is invalid
        messages.error(request, f'error: {e}')
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
        print(user.username + ' just subscribed.')

    return HttpResponse(status=200)
