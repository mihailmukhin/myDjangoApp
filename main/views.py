from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def recipes(request):
    return render(request, 'main/recipes.html')


def categories(request):
    return render(request, 'main/categories.html')
