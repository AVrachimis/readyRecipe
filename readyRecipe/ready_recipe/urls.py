from django.urls import path
from ready_recipe import views

app_name = 'ready_recipe'
urlpatterns = [
    path('', views.index, name='index'),
    ]