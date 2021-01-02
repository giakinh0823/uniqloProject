from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'register'

urlpatterns = [
    path('signup/', views.signup, name ='signup'),
    path('login/', views.loginuser, name ='login'),
    path('logout/', views.logoutuser, name='logout')
]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)