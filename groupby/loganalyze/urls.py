from django.urls import path
from . import views

app_name = 'loganalyze'

urlpatterns = [
    path('', views.main, name='main'),
]