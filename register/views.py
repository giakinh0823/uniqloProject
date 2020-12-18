from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserProfileForm , UserForm
from django.contrib.auth.decorators import login_required,user_passes_test

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
            return redirect('home:index')
        
@login_required
def logoutuser(request):
    if request.method=="POST":
        logout(request)
        return redirect('home:index')
    
