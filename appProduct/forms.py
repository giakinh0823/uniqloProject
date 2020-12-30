from django import forms
from django.db import models
from django.forms import widgets
from .models import ImageProduct, Product, Category , Variants, Size, Color
from django.forms.models import ModelMultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple




class ImageProductForm(forms.ModelForm):
    class Meta():
        model = ImageProduct
        fields = ('name', 'image')


class ProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = ('name', 'price','category', 'quantity','recommend','image')
        
        
class CustomSelectMultiple(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s" %(obj.name)
    
    
class VariantsForm(forms.ModelForm):
    # imageProduct = forms.ImageField()
    
    # SIZE_CHOICES = (
    #     ('XS','XS'),
    #     ('S','S'),
    #     ('M','M'),
    #     ('L','L'),
    #     ('XL','XL'),
    #     ('XXL','XXL'),
    #     ('3XL','3XL'),
    # )
    # size = forms.MultipleChoiceField(choices=SIZE_CHOICES,widget=forms.CheckboxSelectMultiple)
    size = CustomSelectMultiple(widget=forms.CheckboxSelectMultiple, queryset=Size.objects.all())
    color = CustomSelectMultiple(widget=forms.CheckboxSelectMultiple, queryset=Color.objects.all())
    imageProduct = CustomSelectMultiple(widget=forms.CheckboxSelectMultiple, queryset=ImageProduct.objects.all())
    class Meta():
        model = Variants
        fields = ('gender','size','color', 'quantity', 'price', 'imageProduct')
