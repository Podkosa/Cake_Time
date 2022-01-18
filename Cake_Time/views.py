from django.views import generic

class HomePageView(generic.TemplateView):
    template_name = 'homepage.html'
    context_object_name = 'homepage'

class AboutView(generic.TemplateView):
    template_name = 'about.html'
    context_object_name = 'about'