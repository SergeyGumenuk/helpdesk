from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from products.forms import CreateProductForm
from products.models import Product


def get_catalog(request):
    products = Product.available.all()
    return render(request, 'products/catalog.html', {'products': products})


def get_product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug)
    return render(request, 'products/detail.html', {'product': product})


def add_product_to_catalog(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('products:catalog'))
    else:
        form = CreateProductForm()

    return render(request, 'products/add_product.html', {'form': form})
