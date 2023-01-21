from django import forms

from products.models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'slug', 'description', 'price']
