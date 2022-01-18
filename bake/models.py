from django.db import models

# Create your models here.

class Cake(models.Model):
    cake_name = models.CharField (max_length=20, unique=True)
    img = models.ImageField (upload_to='cakes')
    composition = models.ManyToManyField ('Ingredient')
    def __str__(self):
        return self.cake_name

    # def get_absolute_url(self):
    #     return reverse_lazy('cake', current_app='shelf', urlconf='shelf.urls', kwargs={'pk' : self.pk})

class Ingredient(models.Model):
    ingredient_name = models.CharField (max_length=20, unique=True)
    in_cakes = models.ManyToManyField ('Cake', blank=True)

    def __str__(self):
        return self.ingredient_name   
