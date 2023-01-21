from django.shortcuts import render, get_object_or_404

from products.models import Product


def get_catalog(request):
    products = Product.available.all()
    return render(request, 'products/catalog.html', {'products': products})


def get_product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug)
    return render(request, 'products/detail.html', {'product': product})
