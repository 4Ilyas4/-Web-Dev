from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category
from rest_framework import generics
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

#REST вьюшки которые насследуются от generic с готовой реализацией операции методов(которые в запросе HTTP)

class ProductsListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all() #все продукты
    serializer_class = ProductSerializer #сериализатор, для пробразования информации в виде модели продукта
    #в формат JSON для возврата в ответе на запросы

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'id' # определяем имя URL-параметра, по которому будет производиться поиск продукта

class CategoriesListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()# все категории
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'id'

class CategoryProductsListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self): 
        category_id = self.kwargs['id'] 
        return Product.objects.filter(category__id=category_id)
    # Метод, который определяет запрос к базе данных для 
    #получения списка продуктов в указанной категории.
    # Он извлекает идентификатор категории из URL-параметров
    # и фильтрует объекты продуктов по этому идентификатору.

#view - представляет собой часть приложения, которая отвечает за обработку
# запросов от клиента (обычно веб-браузера) и формирование ответа.
# В Django, view является функцией Python или методом класса,
# которая принимает запрос HTTP и возвращает ответ HTTP.
#Представление определяет логику обработки запросов от клиентов. 
#Это может включать в себя получение данных из базы данных, 
#выполнение каких-либо вычислений или обработку входных данных.
#После обработки запроса представление формирует ответ,
# который будет отправлен клиенту. Это может быть HTML-страница,
# JSON-ответ,  файл и т. д.
#В представлении часто используются шаблоны для формирования HTML-ответа. 
#Шаблоны позволяют разделить логику и представление данных.
#REST API представления: В приложениях, использующих RESTful архитектуру, 
#представления могут также служить для обработки запросов API.
# Вместо HTML-ответов представления возвращают данные в формате JSON или XML.
#REST = HTTP (GET, POST, PUT, DELETE)
#