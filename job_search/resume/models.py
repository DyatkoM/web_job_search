from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Resume(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(null=True, blank=True)
    salary = models.IntegerField(default=0, null=True, blank=True)
    work_experience = models.CharField(null=True, blank=True)
    contacts = models.CharField(null=True, blank=True)
    skills = models.CharField(null=True, blank=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['time']

    objects = models.Manager()
