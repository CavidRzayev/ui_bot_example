from django.urls import path
from logs.views import AddLogAPIView

urlpatterns = [
    path('add/', AddLogAPIView.as_view(), name='add_log')
]