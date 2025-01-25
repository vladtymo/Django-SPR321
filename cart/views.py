from django.shortcuts import redirect, render
from django.contrib import messages

from cart.cart import add_to_cart, clear_cart, get_cart_items
from products.models import Product

def index(request):
    items = get_cart_items(request.session)
    products = Product.objects.filter(id__in=items.keys())

    # with_quantity = [{ **user.__dict__, 'quantity': items[str(user.id)]} for user in users]

    return render(request, 'cart/index.html', {'products': products})

def add(request, id):

    if Product.objects.get(pk=id) is None:
        messages.error(request, 'Product not found!')
        return redirect('/cart')

    add_to_cart(request.session, id)
    messages.success(request, 'Product added to cart')

    return redirect('/cart')

def clear(request):
    clear_cart(request.session)
    return redirect('/cart')