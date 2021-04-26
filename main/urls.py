from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recipes', views.recipes, name='recipes'),
    path('categories', views.recipes, name='categories')
]
