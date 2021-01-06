from django import forms
from .models import Order



class StateFormOrder(forms.Form):
    class  Meta():
        model = Order
        fields = ('state')