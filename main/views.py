from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipes
from django.db.models import Q
from .forms import RecipeForm


def index(request):
    return render(request, 'main/index.html')


def get_recipes(request):
    search_query = request.GET.get('search', '')
    if search_query:
        recipes = Recipes.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    else:
        recipes = Recipes.objects.order_by('id')

    return render(request, 'main/recipes/recipes.html', {'recipes': recipes})


def show_recipe(request, recipe_id):
    recipe = Recipes.objects.get(pk=recipe_id)
    context = {
         'recipe': recipe,
     }
    return render(request, 'main/recipes/recipe.html', context)
    # return HttpResponse(f"{recipe_id}")


def add(request):
    error = ''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes')
        else:
            error = 'Форма была не верной'
    form = RecipeForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/recipes/add.html', context)
