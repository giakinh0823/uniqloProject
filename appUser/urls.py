from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = 'appUser'

urlpatterns = [
    path('userInfo/', views.userInfo, name ='userInfo'),
    path('editInfo/', views.editInfo, name ='editInfo'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='user/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='user/password-reset/password_reset.html',
             subject_template_name='user/password-reset/password_reset_subject.txt',
             email_template_name='user/password-reset/password_reset_email.html',
             success_url='/login/'
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

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
