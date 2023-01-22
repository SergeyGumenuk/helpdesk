from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from products.forms import CreateUpdateProductForm, UpdateProductForm
from products.models import Product


def get_catalog(request):
    products = Product.objects.all()
    return render(request, 'products/catalog.html', {'products': products})


def get_product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug)
    return render(request, 'products/detail.html', {'product': product})


def add_product_to_catalog(request):
    if request.method == 'POST':
        form = CreateUpdateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('products:catalog'))
    else:
        form = CreateUpdateProductForm()

    return render(request, 'products/add_product.html', {'form': form})


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = CreateUpdateProductForm(instance=product,
                                       data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:detail', form.cleaned_data['slug'])
    else:
        form = CreateUpdateProductForm(instance=product)

    return render(request, 'products/update.html', {'form': form})


def delete_product_from_catalog(request, product_id):
    Product.objects.get(pk=product_id).delete()
    return redirect(reverse_lazy('products:catalog'))
