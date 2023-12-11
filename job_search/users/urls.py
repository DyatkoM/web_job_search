from django.urls import path
from .views import login, registration
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', LogoutView.as_view(next_page='main_page'), name='logout')
]
