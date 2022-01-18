from django.shortcuts import render, redirect
from .models import Cake, Ingredient
from django.views import generic
from random import choice

class CakeHome(generic.TemplateView):
    template_name = 'bake.html'
    def get_context_data(self):
        return {"Ingredients":Ingredient.objects.all()}

def bake(request):
    """Finds cakes with ingredients, chooses 1 randomly, renders a standard cake page. Checks for no ingredients and no matching cake, returns relevant .html"""
    if not list(request.GET.values()): #checks if no ingredients were chosen
        return render(request, 'no_ingredients.html')
    ingredients_id = set(map(int,set(request.GET.values())))
    matching_cakes = []
    for cake in Cake.objects.all():
        ingredients_iter = cake.composition.values_list('id', flat=True)
        if ingredients_id.issubset(set(ingredients_iter)):
            matching_cakes.append(cake)
    if not matching_cakes:
        return render(request, 'too_complicated.html')
    cake = choice(matching_cakes)
    return redirect('shelf:cake', cake.pk)