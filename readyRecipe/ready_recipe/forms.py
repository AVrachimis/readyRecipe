from django import forms
from ready_recipe.models import Category,Recipe,Quantities


"""


class Recipe(forms.ModelForm):
    name = forms.CharField(max_length=300,help_text = "Recipe Title")
    picture = forms.ImageField()
    instuction = forms.CharField(widget=forms.Textarea)
    category = forms.CharField

"""