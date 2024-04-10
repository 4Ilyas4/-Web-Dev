
from rest_framework import serializers
from .models import Product, Category
#сериализаторы для двух моделей которые наследуется от ModelSerializer они используются в представлениях
class ProductSerializer(serializers.ModelSerializer):
    class Meta: # используется в ModelSerializer
        model = Product
        #модель которая сериализуется
        fields = ['id', 'name', 'price', 'description', 'count', 'is_active','categroy']
        #Это список полей модели, которые должны быть сериализованы

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
