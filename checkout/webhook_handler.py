from django.http import HttpResponse

from .models import Order, OrderLine, DeliveryType
from products.models import Product

import json


class StripeWH_Handler:
    """
    Handle Stripe Webhook events
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles webhook events other than payment succeeded
        and payment failed
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handles payment succeeded webhook event
        """
        # Get variables from stripe intent object
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_details = intent.metadata.save_details
        billing = intent.charges.data[0].billing_details
        shipping = intent.shipping

        # getting first and last names from 'name' in stripe
        first_name = shipping.name.split(" ")[0]
        last_name = shipping.name.split(" ")[1]

        # Get Delivery Type instance
        delivery_type_value = shipping.carrier
        delivery_type = DeliveryType.objects.get(id=delivery_type_value)

        # convert total amount from an integer to a decimal number
        total = round(intent.charges.data[0].amount / 100, 2)

        # Make sure data passed into shipping is not empty string and
        # is stored as Null instead
        for field, value in shipping.address.items():
            if value == "":
                shipping.address[field] = None

        """
        Set order_exist to False, then look for an order matching
        the fields from the checkout form. If order exists, we return
        status code 200, if not, order is created.
        """
        order_exists = False
        try:
            order = Order.objects.get(
                first_name__iexact=first_name,
                last_name__iexact=last_name,
                email__iexact=billing.email,
                phone_number__iexact=shipping.phone,
                address_line_1__iexact=shipping.address.line1,
                address_line_2__iexact=shipping.address.line2,
                city__iexact=shipping.address.city,
                region__iexact=shipping.address.state,
                country__iexact=shipping.address.country,
                postcode__iexact=shipping.address.postal_code,
                delivery_type=delivery_type,
                total=total,
            )
            order_exists = True

            # Return 200 response in case order exists
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]}'
                        ' - Order already exists',
                status=200)

        except Order.DoesNotExist:
            try:
                # Create and populate order model
                order = Order.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=billing.email,
                    phone_number=shipping.phone,
                    address_line_1=shipping.address.line1,
                    address_line_2=shipping.address.line2,
                    city=shipping.address.city,
                    region=shipping.address.state,
                    country=shipping.address.country,
                    postcode=shipping.address.postal_code,
                    delivery_type=delivery_type,
                )
                # loop through cart items data gotten from intent
                for product_id, qty in json.loads(cart).items():
                    product = Product.objects.get(id=product_id)
                    # Add product and order details to order line
                    order_line = OrderLine(
                        order=order,
                        product=product,
                        quantity=qty,
                    )
                    order_line.save()
            # I an error occurs, delete order and display error
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} - {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles payment failed webhook event
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
