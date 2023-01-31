from django.urls import path
from forkrepo import views

urlpatterns = [
    path('', views.index, name='index'),

]
