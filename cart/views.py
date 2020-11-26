from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view that show all the plant's the customer wants"""
    return render(request, 'cart/cart.html')
