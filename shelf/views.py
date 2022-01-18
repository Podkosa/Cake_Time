from bake.models import Cake
from django.views import generic

class CakeDetail (generic.DetailView):
    model = Cake
    template_name = 'cake.html'
    context_object_name = 'cake'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.composition.all()
        return context
    
class Shelf(generic.ListView):
    model = Cake
    template_name = 'shelf.html'
    context_object_name = 'cakes'