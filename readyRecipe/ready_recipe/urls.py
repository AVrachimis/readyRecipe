from django.urls import path
from ready_recipe import views

app_name = 'ready_recipe'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),  
    path('category/<slug:category_name_slug>/<slug:recipe_name_slug>/',views.show_recipe, name='show_recipe'),
    path('add_recipe/',views.add_recipe,name = 'add recipe') ,

    ]