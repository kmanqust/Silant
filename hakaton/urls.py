from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search_view, name='search_view'),
    path('silant/', views.gg, name='silant'),
]