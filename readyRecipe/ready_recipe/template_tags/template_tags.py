from django import template
from ready_recipe.models import Category,Recipe

register = template.Library()

@register.inclusion_tag('ready_recipe/categories.html')


def get_category_list():
    context_dict={}
    categories = Category.objects.all()
    recipes = Recipe.objects.all()
    context_dict['categories'] = categories
    context_dict['recipes'] = recipes

    return context_dict
    


