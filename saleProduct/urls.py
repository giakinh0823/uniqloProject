"""saleProduct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    #home
    path('',include('home.urls')),
    #user
    path('',include('appUser.urls')),
    #register
    path('',include('register.urls')),
    #product
    path('',include('appProduct.urls')),
    #auth
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='user/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
    #order
    path('', include('order.urls')),
    #favourite
    path('', include('favourite.urls')),
    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
            template_name='user/password-reset/password_reset.html',
            subject_template_name='user/password-reset/password_reset_subject.txt',
            email_template_name='user/password-reset/password_reset_email.html',
            # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='user/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='user/password-reset/password_reset_confirm.html'
        ),
        name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='user/password-reset/password_reset_complete.html'
        ),
        name='password_reset_complete'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)