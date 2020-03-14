from django.urls import path
from ready_recipe import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'ready_recipe'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),  
    path('category/<slug:category_name_slug>/<slug:recipe_name_slug>/',views.show_recipe, name='show_recipe'),
    path('add_recipe/',views.add_recipe,name = 'add recipe') ,
    path('profile/',views.user_profile,name='user_profile'),
    path('register/',views.register,name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    