from django.urls import path 

from .views import translate , home

urlpatterns = [
    path('' , home ),
    path('result/<str:noun>/' , translate , name='result' ),
]