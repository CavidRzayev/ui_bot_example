from app.views import *
from django.urls import path
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path("ask_stream/", save,name="ask_stream"),
]
