
from rest_framework import viewsets
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

class CompanyListViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_url_kwarg = 'id'

class CompanyVacancyListView(viewsets.ModelViewSet):
    serializer_class = VacancySerializer
     
    def get_queryset(self):
        id = self.kwargs['id']
        return Vacancy.objects.filter(company = id)

class VacancyListViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDetailViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_url_kwarg = 'id'

class TopTenVacancyListViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.order_by('-salary')[:10]
    serializer_class = VacancySerializer
