from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from store.models import Product
from .cart import Cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    override_quantity = bool(request.POST.get('override'))
    
    cart.add(product=product, quantity=quantity, override_quantity=override_quantity)
    messages.success(request, f'{product.name} added to cart!')
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.warning(request, f'{product.name} removed from cart!')
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart})