from django.urls import path
from .views import *
urlpatterns = [
    path("suv/",suview),
    path("liv/",liview),
    path("lov/",loview),
]