"""
URL configuration for ui_bot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import index,save,gtp,detail,create_detail
from django.conf import settings
from django.conf.urls.static import static
from user.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("save/",save,name="save"),
    path("gtp/",gtp,name="gtp"),
    path("auth/",include("user.urls")),
    path("detail/<id>/",detail,name="detail"),
    path("create/",create_detail,name="create_detail")
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
