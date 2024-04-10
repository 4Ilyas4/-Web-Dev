from django.contrib import admin
from .models import Product, Category
# Register your models here.
#используется для регистрации моделей в административном интерфейсе Django
admin.site.register(Product)
admin.site.register(Category)
