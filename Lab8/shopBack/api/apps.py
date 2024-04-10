from django.apps import AppConfig
#импортирует класс `AppConfig` из модуля `django.apps`.
# `AppConfig` используется для настройки конфигурации Django-приложения.

class ApiConfig(AppConfig):
    #Здесь определяется класс `ApiConfig`, который является подклассом `AppConfig`. 
    #Он представляет конфигурацию для приложения с именем `api`.
    default_auto_field = 'django.db.models.BigAutoField' #определяет значение `default_auto_field`
    #Здесь устанавливается тип автоинкрементного поля, используемый Django для моделей.
    #BigAutoField - это тип поля для больших целых чисел, который Django использует по умолчанию в новых проектах.
    name = 'api'



