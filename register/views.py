from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserProfileForm , UserForm
from django.contrib.auth.decorators import login_required,user_passes_test
from order.models import Cart
from order.views import carts
from appProduct.models import Product
from django.contrib import messages


@user_passes_test(lambda u: u.is_anonymous, login_url='home:index')
def signup(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if request.POST['password']==request.POST['password1']:
            if user_form.is_valid() and profile_form.is_valid():
                user= user_form.save() 
                user.set_password(user.password) 
                user.save()
                profile= profile_form.save(commit=False)
                profile.user = user
                if 'avatar' in request.FILES:
                    profile.avatar = request.FILES['avatar']
                profile.save()
                login(request, user)
                return redirect('home:index')
            else:
                return render(request, 'register/signup.html', {'user_form': user_form, 'profile_form': profile_form, 'error': "Wrong fomat"})
        else:
            return render(request, 'register/signup.html', {'user_form': user_form, 'profile_form': profile_form, 'error': "Password Wrong"})
    else:
        user_form = UserForm()
        profile_form= UserProfileForm()
    return render(request, 'register/signup.html', {'user_form': user_form, 'profile_form': profile_form})

@user_passes_test(lambda u: u.is_anonymous, login_url='home:index')
def loginuser(request):
    if request.method == "GET":
        return render(request, 'register/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'register/login.html', {'form': AuthenticationForm(), 'error': "username or password wrong"})
        else: 
            login(request, user) 
            
            #nếu như có session thì thêm vào cart
            try:
                cartInfo = request.session['carts']
            except:
                cartInfo = None
            if cartInfo != None:
                for key, value in cartInfo.items():
                    productDetail = Product.objects.get(id=key)
                    try:
                        cartItem = Cart.objects.get(product = productDetail,user = user)
                    except Cart.DoesNotExist:
                        cartItem = None
                    if cartItem != None:
                        cartItem.quantity = int(value['num'])
                        cartItem.save()
                    else:
                        newCartItem = Cart(user = request.user, product = productDetail,quantity = int(value['num'])) 
                        newCartItem.save()
                quantity=0
                listCart = Cart.objects.filter(user = user)
                for item in listCart:
                    quantity += int(item.quantity)
                request.session['quantity']=quantity   
            return redirect('home:index')
        
@login_required
def logoutuser(request):
    carts.clear()
    try:
        for key in list(request.session.keys()):
            del request.session[key]
    except KeyError:
        pass
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    else:
        request.session.set_test_cookie()
    if request.method=="POST":
        logout(request)
        return redirect('home:index')
    
