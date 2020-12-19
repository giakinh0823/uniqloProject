#url
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

#import register
from register.models import UserProfile
from register.forms import UserProfileForm , UserForm

#login register
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required,user_passes_test

#change password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

@login_required
def userInfo(request):
    userInfo = UserProfile.objects.filter(user = request.user)[0]
    return render(request, 'user/userInfo.html', {'userInfo': userInfo})

@login_required
def editInfo(request):
    userProfile = get_object_or_404(UserProfile , user=request.user)
    form = UserProfileForm(instance=userProfile)
    if request.method == "GET": 
        form = UserProfileForm(instance=userProfile)
        return render(request, 'user/editInfo.html', {'userProfile' : userProfile , 'form': form})
    else:
        try:
            if 'avatar' in request.FILES:
                userProfile.avatar = request.FILES['avatar']
            form = UserProfileForm(request.POST, instance = userProfile)
            form.save()
            return redirect('appUser:userInfo')
        except:
            return render(request, 'user/editInfo.html', {'userProfile' : userProfile ,'form':form, 'error': "Wrong fomat"})