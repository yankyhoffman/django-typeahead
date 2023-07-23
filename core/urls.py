from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
