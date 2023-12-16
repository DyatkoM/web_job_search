from django.urls import path
from .views import resume_create, ShowResume

urlpatterns = [
    path('all_resume/', ShowResume.as_view(), name='all_resume'),
    path('create_resume/', resume_create, name='resume_create'),

]
