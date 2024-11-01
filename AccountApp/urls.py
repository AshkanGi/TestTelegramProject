from django.urls import path
from . import views

app_name = 'AccountApp'
urlpatterns = [
    path('', views.Login.as_view(), name='login'),
]