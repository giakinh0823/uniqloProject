from django.shortcuts import render
from order.models import Cart

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        quantity=0
        listCart = Cart.objects.filter(user = request.user)
        for item in listCart:
            quantity += int(item.quantity)
        request.session['quantity']=quantity
        return render(request, 'home/index.html', {'quantity': quantity})
    else:
        return render(request, 'home/index.html')
