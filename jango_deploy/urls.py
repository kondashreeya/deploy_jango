"""
URL configuration for jango_deploy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from app1.views import std_list,std_update,std_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",std_list,name='home_page'),
    path("update<int:id>/",std_update,name="std_update"),
    path("delete<int:id>/",std_delete,name='std_delete')
]
