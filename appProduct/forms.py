from django import forms
from django.forms import widgets
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = ('name', 'price', 'quantity','recommend','image')