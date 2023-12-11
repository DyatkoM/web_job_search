from django.urls import path
from .views import ShowVacancy

urlpatterns = [
    path('all_vacancy/', ShowVacancy.as_view(), name='all_vacancy')
]
