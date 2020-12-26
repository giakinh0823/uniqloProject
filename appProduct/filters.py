import django_filters
from  django_filters import DateFilter, CharFilter

from  .models import *


class ProductFilter(django_filters.FilterSet):
    # datecreated = DateFilter(field_name = "datecreated", lookup_expr='gte')
    name = CharFilter(field_name = "name", lookup_expr="icontains")
    class Meta():
        model = Product
        fields = ('category' ,'name', 'price', 'quantity','recommend','datecreated')
