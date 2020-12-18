from django.shortcuts import render, redirect,get_object_or_404
from .models import Product
from .forms import ProductForm, Category
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils import timezone
# Create your views here.


def product(request):
    products = Product.objects.all()
    return render(request, 'product/product.html', {'products': products})

@login_required
def productuser(request):
    products = Product.objects.filter(user = request.user)
    return render(request, 'product/productuser.html', {'products': products})

@login_required
def createproduct(request):
    if request.method == "GET": 
        categorys = Category.objects.all()
        return render(request, 'product/createproduct.html', {'form': ProductForm(), 'categorys': categorys})
    else:
        form = ProductForm(request.POST)
        product = form.save(commit=False)
        product.user = request.user
        category = str(request.POST['category'])
        product.category = Category.objects.filter(name = category)[0]
        product.save()
        return redirect('appProduct:product')

def detailproduct(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    return render(request, 'product/detailproduct.html', {'product': product})


