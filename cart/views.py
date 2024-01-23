from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from spiceapp.models import product_tbl
from . models import Cart,CartItem,Direct_buy,Buy
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


# ---------- cart view -------------


def _cart_id(request):
    cart = request.user
    user = request.user
    if not cart:
        cart = user
    return cart


@login_required(login_url='spiceapp:login')
def add_cart(request,product_id):
    # idn  = request.GET['idn']
    product = product_tbl.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save(),
    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save(),
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart,
            )
        cart_item.save()

    return redirect('cartapp:cart_detail')

def cart_detail(request,total=0,counter=0,gram=0,cart_items=None):
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
       
        cart_items = CartItem.objects.filter(cart=cart,active=True)
        
        for cart_item in cart_items:
            
            total += (cart_item.product.product_price * cart_item.quantity)
            gram += (cart_item.product.gram_of_product * cart_item.quantity)
            counter += cart_item.quantity
            cart_item.total = total
            cart_item.save()
            
        
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter,gram=gram))



def cart_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(product_tbl,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartapp:cart_detail')

def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(product_tbl, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cartapp:cart_detail')



# ----------- direct buy -------------
def _b_id(request):
    bid = request.user
    user = request.user
    if not bid:
        bid = user
    return bid

@login_required(login_url='spiceapp:login')
def add_buy(request,product_id):
    # idn  = request.GET['idn']
    product = product_tbl.objects.get(id=product_id)
    try:
        buy = Buy.objects.get(b_id=_b_id(request))
    except Buy.DoesNotExist:
        buy = Buy.objects.create(
            b_id = _b_id(request)
        )
        buy.save(),
    try:
        buy_item = Direct_buy.objects.get(product=product,b=buy)
        if buy_item.quantity < buy_item.product.stock:
            buy_item.quantity += 1
        buy_item.save(),
    except Direct_buy.DoesNotExist:
        buy_item = Direct_buy.objects.create(
                product = product,
                quantity = 1,
                b = buy,
            )
        buy_item.save()

    return redirect('cartapp:buy_detail')

def buy_detail(request,total=0,counter=0,gram=0,buy_items=None):
    
    try:
        buy = Buy.objects.get(b_id=_b_id(request))
       
        buy_items = Direct_buy.objects.filter(b=buy,active=True)
        
        for buy_item in buy_items:
            
            total += (buy_item.product.product_price * buy_item.quantity)
            gram += (buy_item.product.gram_of_product * buy_item.quantity)
            counter += buy_item.quantity
            buy_item.total = total
            buy_item.save()
            
        
    except ObjectDoesNotExist:
        pass
    return render(request,'direct_buy.html',dict(buy_items=buy_items,total=total,counter=counter,gram=gram))



def buy_remove(request,product_id):

    buy = Buy.objects.get(b_id=_b_id(request))
    product = get_object_or_404(product_tbl,id=product_id)
    buy_item = Direct_buy.objects.get(product=product,b=buy)
    if buy_item.quantity > 1:
        buy_item.quantity -= 1
        buy_item.save()
    else:
        buy_item.delete()
        return redirect('/')
    return redirect('cartapp:buy_detail')


def buy_full_remove(request,product_id):
    buy = Buy.objects.get(b_id=_b_id(request))

    product = get_object_or_404(product_tbl, id=product_id)
    buy_item = Direct_buy.objects.get(product=product, b=buy)
    buy_item.delete()
    return redirect('/')

