from django.contrib import admin

from bake.models import Ingredient, Cake

# Register your models here.
admin.site.register(Cake)
admin.site.register(Ingredient)