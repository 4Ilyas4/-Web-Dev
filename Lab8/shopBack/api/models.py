from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
#Эти модели Product и Category представляют собой таблицы
#базы данных, которые будут созданы при выполнении
# миграций Django. Каждый экземпляр модели будет представлять
# одну запись в соответствующей таблице, 
#а каждое поле модели будет отображаться в столбце таблицы.
#модель - удобный способ работы с базой данных через объекты Python