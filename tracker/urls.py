from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('income/add/', views.add_income, name='add_income'),
    path('expense/add/', views.add_expense, name='add_expense'),
    path('report/', views.monthly_report, name='report'),
]