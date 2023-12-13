from django.urls import path
from .views import ShowVacancy, vacancy_create

urlpatterns = [
    path('all_vacancy/', ShowVacancy.as_view(), name='all_vacancy'),
    path('create_vacancy/', vacancy_create, name='vacancy_create')
]
