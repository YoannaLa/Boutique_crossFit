from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse
from products.models import Product
from .models import Wishlist

from .models import User


@login_required
def view_wishlist(request):
    """
    A view that displays users wishlist
    """
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})
    wishlist_items_count = 0
    try:
        all_wishlist = Wishlist.objects.filter(username=request.user.id)[0]
    except IndexError:
        wishlist_items = None
    else:
        wishlist_items = all_wishlist.products.all()
        wishlist_items_count = all_wishlist.products.all().count()

    if not wishlist_items:
        messages.info(request, 'Your wishlist is empty!')

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
        'wishlistitems_count': wishlist_items_count
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, item_id):
    """
    A view that will add a product item to list
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        wishlist = get_object_or_404(Wishlist, username=request.user.id)
    except Http404:
        wishlist = Wishlist.objects.create(username=request.user)

    if product in wishlist.products.all():
        messages.info(request, 'The product is already in your wishlist!')
    else:
        wishlist.products.add(product, item_id)
        messages.info(request, 'Added the product to your wishlist')

    return redirect(reverse('product_detail', args=[item_id]))


@login_required
def remove_from_wishlist(request, item_id, redirect_from):
    """
    A view that will add a product item to wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    wishlist = get_object_or_404(wishlist, username=request.user.id)
    if product in wishlist.products.all():
       wishlist.products.remove(product)
       messages.info(request, 'Removed the product '
                               'from your wishlist')
    else:
        messages.error(request, 'That product is '
                                'not in your on your list!')
    if redirect_from == 'wishlist':
        redirect_url = reverse('wishlist')
    else:
        redirect_url = reverse('product_detail', args=[item_id])

    return redirect(redirect_url)
