from django import forms
from .models import Resume


class CreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form_title', 'placeholder': 'Заголовок:'}))
    salary = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form_salary', 'placeholder': 'Заработная плата:'}))
    work_experience = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form_work_experience', 'placeholder': 'Опыт работы:'}))
    conditions = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form_conditions', 'placeholder': 'Условия:'}))
    contacts = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form_contacts', 'placeholder': 'Контакты и адрес:'}))
    skills = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form_skills', 'placeholder': 'Ключевые навыки:'}))

    class Meta:
        model = Resume
        fields = [
            'title', 'salary', 'work_experience',
            'duties', 'requirements', 'conditions',
            'contacts', 'skills'
        ]
