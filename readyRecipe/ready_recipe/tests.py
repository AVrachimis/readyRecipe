from django.test import TestCase

from ready_recipe.models import *
from population_script import populate
import os
from django.urls import reverse



# helper function to create a user object
def create_user():
    user = User.objects.get_or_create(username='testuser',email='test@email.com')
    userProfile = UserProfile.objects.get_or_create(user1 = user,)[0]
    user.set_password('test1234')
    userProfile.save()
    user.save()

    return user

# helper function to create an admin
def create_superuser():
    superuser = User.objects.create_superuser(username='theAdmin',email='theadmin@email.com')
    superuserProfile=UserProfile.objects.get_or_create(user1=superuser)[0]
    superuser.set_password('theadmin1234')
    superuserProfile.save()
    superuser.save()

    return superuser



class ready_recipe_tests(TestCase):


    def test_check_index_template(self):

        response = self.client.get(reverse('ready_recipe:show_category',args=['easter-recipes']))

        response1 = self.client.get(reverse('ready_recipe:index'))
        response2 = self.client.get(reverse('ready_recipe:add_category'))
        response3 = self.client.get(reverse('ready_recipe:add_recipe'))
        response4 = self.client.get(reverse('ready_recipe:user_profile'))
        response5 = self.client.get(reverse('ready_recipe:register'))
        response6 = self.client.get(reverse('ready_recipe:login'))
        response8 = self.client.get(reverse('ready_recipe:change_password'))
        response9 = self.client.get(reverse('ready_recipe:change_password'))
        response10 = self.client.get(reverse('ready_recipe:show_category',args=['pork']))
        response10 = self.client.get(reverse('ready_recipe:show_recipe',args=['pork','pork-dumplings']))



        self.assertTemplateUsed(response1, 'ready_recipe/index.html')
        #self.assertTemplateUsed(response2, 'ready_recipe/add_category.html')
        #self.assertTemplateUsed(response3, 'ready_recipe/add_recipe.html')
        #self.assertTemplateUsed(response4, 'ready_recipe/user_profile.html')
        #self.assertTemplateUsed(response5, 'ready_recipe/register.html')
        #self.assertTemplateUsed(response6, 'ready_recipe/login.html')
        #self.assertTemplateUsed(response8, 'ready_recipe/change_password.html')


        self.assertTemplateUsed(response1, 'ready_recipe/base.html')
        #self.assertTemplateUsed(response2, 'ready_recipe/base.html')
        #self.assertTemplateUsed(response3, 'ready_recipe/base.html')
        #self.assertTemplateUsed(response4, 'ready_recipe/base.html')
        #self.assertTemplateUsed(response5, 'ready_recipe/base.html')
        #self.assertTemplateUsed(response6, 'ready_recipe/base.html')
        #self.assertTemplateUsed(response8, 'ready_recipe/base.html')

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

    def test_check_slug_functionality_category(self):
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
            self.assertTrue(self.does_gitignore_includes_database(gitignore_path))

        
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


        
