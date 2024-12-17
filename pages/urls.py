from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index2'),
    path('about',views.about,name='about'),
]

 