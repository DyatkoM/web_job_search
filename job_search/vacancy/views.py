from django.shortcuts import render, redirect
from .models import Vacancy
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from .forms import CreateForm


def vacancy_create(request):
    if request.method == "POST":
        form = CreateForm(data=request.POST)
        if form.is_valid():
            title = request.POST['title']
            user = request.user
            form.instance.user = user  # Привязываем текущего пользователя к полю user
            salary = request.POST['salary']
            work_experience = request.POST['work_experience']
            duties = request.POST['duties']
            requirements = request.POST['requirements']
            contacts = request.POST['contacts']
            skills = request.POST['skills']
            form.save()
            return redirect('all_vacancy')

    else:
        form = CreateForm()
    context = {'form': form}
    return render(request, 'vacancy/create_vacancy.html', context)


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
