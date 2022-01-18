from django.urls import path
from . import views

# URLconf
app_name = 'shelf'

urlpatterns = [
    path('', views.Shelf.as_view(), name='shelf'),
    path('cake/<str:pk>', views.CakeDetail.as_view(), name='cake'),
]

