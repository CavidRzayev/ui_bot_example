from django.contrib import admin
from .models import Message,BaseModels
# Register your models here.

admin.site.register(Message)
admin.site.register(BaseModels)