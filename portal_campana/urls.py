"""portal_campana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from guia_ciudad.views import inicio, listar_comercios, listar_restaurantes, listar_propiedades, listar_clasificados


urlpatterns = [
    path('', inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('herramientas/', include('guia_ciudad.urls')),
    path('comercios/', listar_comercios, name="listar_comercios"),
    path('restaurantes/', listar_restaurantes, name="listar_restaurantes"),
    path('propiedades/', listar_propiedades, name="listar_propiedades"),
    path('clasificados/', listar_clasificados, name="listar_clasificados"),
]

