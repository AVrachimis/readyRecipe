from django.test import TestCase

from ready_recipe.models import *
from population_script import populate
import os
from django.urls import reverse
from django.forms import fields as django_fields
from ready_recipe.forms import *
from django.contrib.auth.models import User
from django.conf import settings






# helper function to create a user object
def create_user(self):
    user = User.objects.get_or_create(username='testuser',email='test@email.com',password = 'test1234')[0]
    userProfile = UserProfile.objects.get_or_create(user1 = user)[0]
    userProfile.save()
    user.save()
    self.client.login(username='testuser',password = 'test1234')

    return user

# helper function to create an admin
def create_superuser(self):
    superuser = User.objects.create_superuser(username='theAdmin',email='theadmin@email.com',password = 'theadmin1234')
    superuserProfile=UserProfile.objects.get_or_create(user1=superuser)[0]
    superuserProfile.save()
    superuser.save()
    self.client.login(username='theAdmin',password = 'theadmin1234')

    return superuser



class ready_recipe_tests(TestCase):


    def test_check_index_template(self):

        response = self.client.get(reverse('ready_recipe:index'))
 
        self.assertTemplateUsed(response, 'ready_recipe/index.html')
        self.assertTemplateUsed(response, 'ready_recipe/base.html')
 

    def test_pork_category_content(self):

        populate()
        response = self.client.get(reverse('ready_recipe:show_category',args=['pork']))

        self.assertIn("Roasted Pork Loin".lower(),response.content.decode('ascii').lower())
        self.assertIn("Pork Dumplings".lower(),response.content.decode('ascii').lower())


    def test_vegetarian_category_content(self):

        populate()
        response = self.client.get(reverse('ready_recipe:show_category',args=['vegetarian']))

        self.assertIn("Easy vegetarian tacos".lower(),response.content.decode('ascii').lower())
        self.assertIn("Vegetarian Ravioli".lower(),response.content.decode('ascii').lower())


    def test_check_slug_functionality_category(self):

        category = Category.objects.get_or_create(name='Pork')[0]
        category.name='PORK and LamB'
        category.save()
        self.assertEquals('pork-and-lamb',category.slug,'When the name of the category is changed, slug does not update')


    def test_check_slug_functionality_recipe(self):
        populate()
        recipe = Recipe.objects.get_or_create(name='Carrot soup')[0]
        recipe.name = 'CarROT SOUP with MEat'
        recipe.save()
        self.assertEquals('carrot-soup-with-meat',recipe.slug,'When the name of the recipe is changed, slug does not update')


    def test_empty_category(self):

        category = Category.objects.get_or_create(name='Easter')[0]
        response = self.client.get(reverse('ready_recipe:show_category',args=['easter']))
        self.assertIn("No recipes currently in this category.".lower(),response.content.decode('ascii').lower(),'Wrong message when category has no recipes')


    def test_category_doesnt_exist_message(self):

        populate()
        response = self.client.get(reverse('ready_recipe:show_category',args=['easter-recipes']))
        self.assertIn("The specified category does not exist.".lower(), response.content.decode('ascii').lower(),'Wrong message when the category does not exist')
        

    def test_recipe_doesnt_exist_message(self):

        populate()
        response = self.client.get(reverse('ready_recipe:show_recipe',args=['pork','meatballs']))
        self.assertIn("Recipe not available".lower(), response.content.decode('ascii').lower(),'Wrong message when the recipe does not exist')


    def test_profile_message_without_recipes(self):
        user = create_superuser(self)
        response = self.client.get(reverse('ready_recipe:user_profile'))
        self.assertIn("No recipe uploaded by you!".lower(),response.content.decode('ascii').lower())
        self.assertIn("You have no saved recipes.".lower(),response.content.decode('ascii').lower())


    def does_gitignore_includes_database(self,path):
        f = open(path, 'r')
        
        for line in f:
            line = line.strip()
            
            if line.startswith('db.sqlite3'):
                return True
        
        f.close()
        return False

    def test_database_in_gitignore(self):

        git_base_dir = os.popen('git rev-parse --show-toplevel').read().strip()
        gitignore_path = os.path.join(git_base_dir, '.gitignore')

        if os.path.exists(gitignore_path):
            self.assertTrue(self.does_gitignore_includes_database(gitignore_path),'Database is not included in the gitignore. Add it')

        
    def test_recipe_model(self):
        populate()
        chicken = Recipe.objects.get(name='Crispy Chicken Thighs')
        beef = Recipe.objects.get(name='Sweet and sour ribeye steaks')
        lamb = Recipe.objects.get(name='Lahmacun')

        self.assertEqual(chicken.average_overall_price,2.15,'Tests on the Recipe model failed. Check your model and try again!')
        self.assertEqual(beef.portions,'2','Tests on the Recipe model failed. Check your model and try again!')
        self.assertEqual(lamb.difficulty,'5','Tests on the Recipe model failed. Check your model and try again!')



    def test_comment_model(self):
        populate()
        c1 = Comment.objects.get(recommentations="Perfect medium rare steak")
        owner = User.objects.get(username = "AndyGr")
        self.assertEquals(c1.owner_id,owner,'Tests on the Comment model failed. Check your model and try again!')


    def test_content_index(self):
        populate()

        response = self.client.get(reverse('ready_recipe:index'))
        categories = Category.objects.all()

        self.assertCountEqual(response.context['categories'], categories,'Index page does not display all the categories')


    def test_add_category_not_in_plain_users(self):
        user = create_user(self)
        response = self.client.get(reverse('ready_recipe:index'))
        self.assertTrue('Add Category'.lower() not in response.content.decode('ascii').lower(),"Add category button should not be displayed unless you are admin")


    def test_add_category_only_at_userusers(self):
        superuser = create_superuser(self)
        response = self.client.get(reverse('ready_recipe:index'))
        self.assertTrue('Add Category'.lower() in response.content.decode('ascii').lower(),"Add category button has to be displayed since the current user is an admin")


    def test_message_when_search_has_no_results(self):
        
        response = self.client.get(reverse('ready_recipe:search', args=['Cheese',None]))
        self.assertIn('No results found for "Cheese"'.lower(),response.content.decode('ascii').lower(),'Wrong message when no results are found on search')
    
    
    def test_empty_search_list(self):
        populate()
        response = self.client.get(reverse('ready_recipe:search', args=[' ',None]))
        recipes = Recipe.objects.all()
        self.assertCountEqual(response.context['all_recipes'], recipes,'Search does not include all the recipes when empty string is searched')


    def test_add_category_form(self):
        superuser = create_superuser(self)
        response = self.client.get(reverse('ready_recipe:add_category'))
        self.assertTrue("Add a Category".lower() in response.content.decode('ascii').lower(),"Add category form is not displayed correctly")


    def test_base_template_exists(self):
                
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'ready_recipe', 'base.html')

        self.assertTrue(os.path.exists(template_base_path),"base.html does not exist in the right directory")








