from django.http import HttpResponse


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
        intent = event.data.object
        print(intent)
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
