"""
URL configuration for hhBack project.

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
from django.urls import path, re_path
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies', views.CompanyListViewSet.as_view({'get': 'list', 'post': 'create'}), name='company-list'), 
    path('api/companies/<int:id>/',views.CompanyDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}, name='company-details')), 
    path('api/companies/<int:id>/vacancies/',views.CompanyVacancyListView.as_view({'get': 'list'}), name='company-vacancy-list'), 
    path('api/vacancies/',views.vacancy_list, name='vacancy-list'), 
    path('api/vacancies/<int:id>/',views.vacancy_detail, name='vacancy-details'), 
    path('api/vacancies/top_ten/',views.top_ten_vacancies, name='top-ten-vacancy'),
    re_path(r'^.*$', views.invalid_url, name='invalid-url')
]
