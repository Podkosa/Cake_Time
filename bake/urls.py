from django.urls import path
from . import views

# URLconf
app_name = 'bake'

urlpatterns = [
    path('', views.CakeHome.as_view(), name='cakehome'),
    path('cake', views.bake, name='bake'),
]

