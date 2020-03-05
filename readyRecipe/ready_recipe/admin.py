from django.contrib import admin
from django.contrib.auth.models import User


from ready_recipe.models import Category,Recipe,Comment,UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepolulated_fields = {'slug':('name')}
    list_display = ['name']

class RecipeAdmin(admin.ModelAdmin):
    prepolulated_fields = {'slug':('name')}
    list_display = ['name','picture','portions','difficulty','category_id','owner_id','views']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['date','recommentations','recipe_id','owner_id']



#class UserProfileAdmin(admin.ModelAdmin):
  #  prepolulated_fields = {'slug':('first_name')}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(UserProfile,)

     #UserProfileAdmin)
