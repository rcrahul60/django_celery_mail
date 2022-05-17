from django.urls import path
from .views import *

urlpatterns = [
    
    path('register/',RegistrationView,name="register"),
    path('login/',login,name="login"),
    path('mail/',sendMail,name="mail"),
]