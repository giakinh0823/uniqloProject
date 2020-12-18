from django.shortcuts import render,redirect,get_object_or_404
from register.models import UserProfile
# Create your views here.


def userInfo(request):
    userInfo = UserProfile.objects.filter(user = request.user)[0]
    return render(request, 'user/userInfo.html', {'userInfo': userInfo})