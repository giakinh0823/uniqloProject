from django import forms
from django.contrib.auth.models import User
from django.forms.fields import DateField
from .models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password','password1')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields= ('first_name','last_name','birth_date','site', 'avatar')
        