from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, ProductImage

# Create your views here.

def all_products(request):
    """ This view will show all products, including sorting and search functionality """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Oops, try using your words!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def extra_view(request, product_id):
    """ This will display extra images if the product contains it """
    product = get_object_or_404(Product, pk=product_id)
    photos = ProductImage.objects.filter(product=product)

    context = {
        'product': product,
        'photos': photos
    }
    return render(request, 'products/extra.html', context)


def product_detail(request, product_id):
    """ This view will show each individual plant's details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
