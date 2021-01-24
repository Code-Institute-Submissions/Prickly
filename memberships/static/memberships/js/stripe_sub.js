// The following code was taken from
// https://testdriven.io/blog/django-stripe-subscriptions/
// and
// https://stripe.com/docs/billing/subscriptions/checkout
// It is used to set up Stripe external checkout form
// to handle subscriptions


// Get Stripe public key
fetch("/config/")
// convert to JS object
.then((result) => { return result.json(); })
// Get data
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
});