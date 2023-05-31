from django.urls import path

from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.payments_summary, name='payments_summary'),
    path('add/', views.payments_add, name='payments_add'),
]