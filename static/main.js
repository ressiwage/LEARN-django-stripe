console.log("Sanity check!");

function buy(id) {
  // Get Stripe publishable key
  fetch("/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
      // Initialize Stripe.js
      const stripe = Stripe(data.publicKey);
      // Get Checkout Session ID
      fetch(`/buy/${id}`)
        .then((result) => { return result.json(); })
        .then((data) => {
          console.log(data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({ sessionId: data.sessionId })
        })
        .then((res) => {
          console.log(res);
        });
    });
}