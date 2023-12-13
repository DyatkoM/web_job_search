from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class Vacancy(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(validators=[RegexValidator(r'^.{0,6000}$', message='текст покороче пожалуйста'), ],
                             null=True, blank=True)
    salary = models.CharField(
        validators=[RegexValidator(r'^\d{1,5}$',
                                   message='вы точно будете столько? '
                                           '(Зарплата должна быть в пределе от 1 Br до 100000Br)')], null=True,
        blank=True)
    work_experience = models.CharField(
        validators=[RegexValidator(r'с [0-9]+ до [0-9]+ лет',
                                   message='поле должно совпадать с шаблоном "с число до число лет"'), ],
        null=True, blank=True)
    duties = models.CharField(validators=[RegexValidator(r'^.{0,500}$', message='текст покороче пожалуйста'), ],
                              null=True, blank=True)
    requirements = models.CharField(validators=[RegexValidator(r'^.{0,500}$', message='текст покороче пожалуйста'), ],
                                    null=True, blank=True)
    conditions = models.CharField(validators=[RegexValidator(r'^.{0,500}$', message='текст покороче пожалуйста'), ],
                                  null=True, blank=True)
    contacts = models.CharField(validators=[RegexValidator(r'^.{0,200}$', message='текст покороче пожалуйста'), ],
                                null=True, blank=True)
    skills = models.CharField(validators=[RegexValidator(r'^.{0,50}$', message='текст покороче пожалуйста'), ],
                              null=True, blank=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['time']

    objects = models.Manager()
