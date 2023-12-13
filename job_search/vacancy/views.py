from django.shortcuts import render
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
            if len(salary) > 15000:
                error_message = "А вы точно будете столько платить?)"
                context = {'form': form, 'error_message_salary': error_message}
                return render(request, 'vacancy/create_vacancy.html', context)
            work_experience = request.POST['work_experience']
            duties = request.POST['duties']
            requirements = request.POST['requirements']
            contacts = request.POST['contacts']
            skills = request.POST['skills']
            if len(title) > 6000:
                error_message = "Вы привысили ограничение по символам"
                context = {'form': form, 'error_message_title': error_message}
                return render(request, 'vacancy/create_vacancy.html', context)

            form.save()
            context = {'form': form}
            return render(request, 'vacancy/list_vacancy.html', context)

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
