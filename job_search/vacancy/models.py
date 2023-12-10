from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vacancy(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(null=True, blank=True)
    salary = models.CharField(null=True, blank=True)
    work_experience = models.CharField(null=True, blank=True)
    duties = models.CharField(null=True, blank=True)
    requirements = models.CharField(null=True, blank=True)
    conditions = models.CharField(null=True, blank=True)
    contacts = models.CharField(null=True, blank=True)
    skills = models.CharField(null=True, blank=True)
