from django.urls import path
from .views import ShowVacancy

app_name = 'users'

urlpatterns = [
    path('show_all_vacancy/', ShowVacancy.as_view(), name='all_vacancy'),
]
