from django.contrib import admin
from django.urls import path
from .views import Signupview
from django.contrib.auth.views import LoginView
from .forms import EmailOrUsernameAuthenticationForm

urlpatterns = [
    path('login/',LoginView.as_view(authentication_form=EmailOrUsernameAuthenticationForm),name='login'),
    path('signup/', Signupview.as_view(),name="signup"),

]
