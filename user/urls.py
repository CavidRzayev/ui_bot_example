from django.urls import path,include
from .views import *
urlpatterns = [
    path("login/",logins,name="login"),
    path("register/",register,name="register"),
    path("logout",logouts,name="logout"),
    path("verify",check_verify,name="check_verify")

]