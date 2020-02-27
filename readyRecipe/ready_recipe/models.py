from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Recipe(models.Model):
    name = models.CharField(max_length=300,unique=True)
    instuction = models.CharField(max_length=2000)
    picture = models.ImageField()
    portions = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    completion_time = models.CharField(max_length=100)
    calories = models.IntegerField(default=0)
    average_overall_price = models.FloatField(default=0)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,default = 0)
    #owner_id = models.ForeignKey(User)



    def __str__(self):
        return self.name




class Comment(models.Model):
    date = models.DateField()
    recommentations = models.CharField(max_length=3000)
    #owner_id = models.ForeignKey(User)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
       
    def __str__(self):
        return self.recommentations




class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    #recipe_has_ingredients = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name



