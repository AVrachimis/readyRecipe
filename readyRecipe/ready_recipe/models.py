from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(UserProfile, self).save(*args, **kwargs)




class Ingredient(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


DIFFICULTY = ( ('1','1'),('2','2' ),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10') )
PORTIONS = ( ('1','1'),('2','2' ),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','More than 10') )
TIME_NEEDED = ( ('1','1-15 minutes'),('2','15-30 minutes' ),('3','30-60 minutes'),('4','1-1.30 hours'),('5','1.30-2 hours'),('6','2-2.30 hours'),('7','More than 2.30 hours'),)
class Recipe(models.Model):
    name = models.CharField(max_length=300,unique=True)
    instuction = models.TextField(max_length=2000)
    picture = models.ImageField()
    portions = models.CharField(max_length=30,choices=PORTIONS)
    difficulty = models.CharField(max_length=2,choices=DIFFICULTY)
    completion_time = models.CharField(max_length=30,choices = TIME_NEEDED)
    calories = models.IntegerField(default=0)
    average_overall_price = models.FloatField(default=0)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,default = 0)
    views = models.IntegerField(default=0)
    owner_id = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    ingredient = models.ManyToManyField(Ingredient,through='Quantities')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)



    def __str__(self):
        return self.name


class Quantities(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100,default=0,null=True)
    class Meta:
        verbose_name_plural = 'Quantities'




class Comment(models.Model):
    date = models.DateField()
    recommentations = models.TextField(max_length=3000)
    owner_id = models.ForeignKey(User,on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
       
    def __str__(self):
        return self.recommentations

