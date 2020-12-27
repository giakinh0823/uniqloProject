import django_filters
from  django_filters import DateFilter, CharFilter
from django import forms


from  .models import *


class ProductFilter(django_filters.FilterSet):
    # datecreated = DateFilter(field_name = "datecreated", lookup_expr='gte')
    name = CharFilter(field_name = "name", lookup_expr="icontains")
    category= django_filters.ModelChoiceFilter(queryset=Category.objects.all(),
        widget=forms.RadioSelect)
    class Meta():
        model = Product
        fields = ('category' ,'name')
