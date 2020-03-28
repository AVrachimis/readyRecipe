from django.urls import path
from ready_recipe import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


app_name = 'ready_recipe'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),  
    path('category/<slug:category_name_slug>/<slug:recipe_name_slug>/',views.show_recipe, name='show_recipe'),
    path('add_recipe/',views.add_recipe,name = 'add_recipe') ,
    path('add_category/',views.add_category,name = 'add_category'),
    path('profile/',views.user_profile,name='user_profile'),
    path('register/',views.register,name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login', views.user_login,name='login'),
    url(r'^(?P<primaryKey>\d+)/$',views.add_or_delete_recipe,name = 'add_or_delete_recipe'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search/(?P<search>[\w|\W.-]+)/(?P<sorting>[\w|\W.-]+)/$',views.search,name = 'search'),
    url(r'^delete/(?P<username>[\w|\W.-]+)/$', views.delete_user, name='delete_user'),
    url(r'^password/$', views.change_password, name='change_password'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    