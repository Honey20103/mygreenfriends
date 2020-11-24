from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage

# Create your views here.

def all_products(request):
    """ This view will show all products, including sorting and search functionality """

    products = Product.objects.all()

    context = {
        'products':products,
    }
    return render(request, 'products/products.html', context)


def extra_view(request, id):
    """ This will display extra images if the product contains it """
    product = get_object_or_404(Product, id=id)
    photos = ProductImage.objects.filter(product=product)

    context = {
        'product': product,
        'photos': photos
    }
    return render(request, 'extra.html', context)
