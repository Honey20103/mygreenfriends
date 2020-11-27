from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that show all the plant's the customer wants"""
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ This adds a quantity of chosen plants into the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ This adjusts quantity of chosen plants into the shopping cart """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=item_id)

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request,
                        (f'Updated {product.name} '
                         f'quantity to {cart[item_id]}'))
    else:
        cart.pop(item_id)
        messages.success(request,
                         (f'Removed {product.name} '
                          f'from your cart'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def del_from_cart(request, item_id):
    """Delete the plant from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)

        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
