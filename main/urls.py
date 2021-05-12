from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recipes/', views.get_recipes, name='recipes'),
    path('add/', views.add, name='add'),
    path('recipes/<int:recipe_id>/', views.show_recipe, name='recipe')
]
