from django.shortcuts import render
from .models import Vacancy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ShowVacancy(ListView, LoginRequiredMixin):
    model = Vacancy
    fields = [
        'title', 'salary', 'work_experience',
        'duties', 'requirements', 'conditions',
        'contacts', 'skills'
    ]
    context_object_name = 'all_vacancy'
    template_name = 'vacancy/list_vacancy.html'

