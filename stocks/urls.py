from django.urls import path
from . import views

urlpatterns = [
    path('', views.stocks, name='stocks'),
    path('investment_form/', views.investment_form, name='investment_form'),
]
