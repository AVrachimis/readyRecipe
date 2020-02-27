from django.contrib import admin

from ready_recipe.models import Category,Recipe,Ingredient,Comment


class CategoryAdmin(admin.ModelAdmin):
    prepolulated_fields = {'slug':('name')}

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name','instuction','picture','portions','difficulty','completion_time','calories','average_overall_price','category_id','views']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['date','recommentations','recipe_id']

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Ingredient,IngredientAdmin)
admin.site.register(Comment,CommentAdmin)
