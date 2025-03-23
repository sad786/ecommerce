from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import OrderItem, Order
from cart.cart import Cart

@login_required
def checkout(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        # # Create a new order
        # order = Order.objects.create(
        #     user=request.user,
        #     first_name=request.POST.get('first_name'),
        #     last_name=request.POST.get('last_name'),
        #     email=request.POST.get('email'),
        #     address=request.POST.get('address'),
        #     postal_code=request.POST.get('postal_code'),
        #     city=request.POST.get('city')
        # )
        
        # # Add items from cart to order
        # for item in cart:
        #     OrderItem.objects.create(
        #         order=order,
        #         product=item['product'],
        #         price=item['price'],
        #         quantity=item['quantity']
        #     )
        
        # # Clear the cart
        # cart.clear()
        
        return render(request, 'orders/order_created.html', {'order': ''})
    
    return render(request, 'orders/checkout.html', {
        'cart': cart,
        'paypal_client_id': settings.PAYPAL_CLIENT_ID
    })

@login_required
def order_complete(request):
    order_id = request.GET.get('order_id')
    transaction_id = request.GET.get('transaction_id')
    
    if order_id and transaction_id:
        order = Order.objects.get(id=order_id)
        order.paid = True
        order.paypal_transaction_id = transaction_id
        order.save()
    
    return render(request, 'orders/order_complete.html')