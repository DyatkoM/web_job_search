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
    context_object_name = 'list_vacancy'
    template_name = 'vacancy/list_vacancy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['list_vacancy'] = context['list_vacancy'].filter(title__startswith=search_input)
            context['search_input'] = search_input
        return context
