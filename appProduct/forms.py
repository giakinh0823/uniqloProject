from django import forms
from django.forms import widgets
from .models import Product, Category , Variants, Size, Color


class ProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = ('name', 'price', 'quantity','recommend','image')
        
        
class VariantsForm(forms.ModelForm):
    imageProduct = forms.ImageField()
    
    SIZE_CHOICES = (
        ('XS','XS'),
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('XXL','XXL'),
        ('3XL','3XL'),
    )
    size = forms.MultipleChoiceField(choices=SIZE_CHOICES,widget=forms.CheckboxSelectMultiple)
    class Meta():
        model = Variants
        fields = ('gender', 'size', 'color', 'imageProduct', 'quantity', 'price')