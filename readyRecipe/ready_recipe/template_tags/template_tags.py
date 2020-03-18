from django import template
from rango.models import Category,Recipe

4 register = template.Library()

@register.inclusion_tag('ready_recipe/categories.html')

def category_recipe_list():
    context_dict={}
    categories = Category.Objects.all()

    info = {}
    for category in categories:
        recipes = Recipe.Objects.filter(category_id = category.id)
        recipe_list = []
        for recipe in recipes:
            recipe_list.append(recipe)
        info[category]=recipe_list
        recipe_list=[]
    return context_dict['information']=info
    
