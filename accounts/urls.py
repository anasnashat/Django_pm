from django.urls import include, path
from django.contrib.auth.views import LoginView
from . import forms
urlpatterns = [
    path('login/', LoginView.as_view(authentication_form = forms.UserLoginForm), name ='login' ),
    path('', include('django.contrib.auth.urls'))
]
