from django.urls import path
from . import views

app_name = 'police'

urlpatterns = [
    path('', views.all_fines, name = 'all_fines'),
    path('item/<slug:slug>/', views.fine_detail, name='fine_detail'),
    path('search/<slug:category_slug>/', views.category_list, name = 'category_list'),
]