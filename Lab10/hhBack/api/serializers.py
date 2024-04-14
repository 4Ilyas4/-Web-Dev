from rest_framework import serializers
from .models import Company, Vacancy

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    salary = serializers.FloatField()
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    
#or
# def vacancy_serializer(vacancy):
#     return {
#         'id': vacancy.id,
#         'name': vacancy.name,
#         'description': vacancy.description,
#         'salary': vacancy.salary,
#         'company_id': vacancy.company_id,
#     }