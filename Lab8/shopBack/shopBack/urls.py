"""
URL configuration for shopBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ..api import views

urlpatterns = [
    path('admin/', admin.site.urls), # для административного интерфейса
    path('api/products/', views.ProductsListAPIView.as_view(), name='product-list'), # .as_view() для преобразования класса представления в функцию представления
    path('api/products/<int:id>/', views.ProductDetailAPIView.as_view(), name='product-detail'),#  name это имя пути которое юзается в html 
    path('api/categories/', views.CategoriesListAPIView.as_view(), name='category-list'),       #  или во вьюшке к примеру для return redirect('product-list')
    path('api/categories/<int:id>/', views.CategoryDetailAPIView.as_view(), name='category-detail'),
    path('api/categories/<int:id>/products/', views.CategoryProductsListAPIView.as_view(), name='category-product-list'),
]
#здеь при использовании какого либо пути просиходит работа вьюшки этого пути которая отвечает на запрос 

