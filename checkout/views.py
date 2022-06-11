from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings 

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "The basket is empty!")
        return redirect(reverse('products'))


    current_bag = bag_contents(request)
    total = current_bag ['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L97OiCQmncmYtAI6SLhmDxcIz5WtL6dFY8FwdNdabzRSBpGJDqmRRVNCNp1KoiWNB62mkYMb6iqf6F17AqHKhHe0040jj77gm',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
