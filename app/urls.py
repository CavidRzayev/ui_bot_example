from app.views import AskStreamAPIView
from django.urls import path

urlpatterns = [
    path("ask_stream/", AskStreamAPIView.as_view(), name="ask_stream"),
]
