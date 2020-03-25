import os
import datetime
from django.template.defaultfilters import slugify


os.environ.setdefault('DJANGO_SETTINGS_MODULE','readyRecipe.settings')


import django
django.setup()
from ready_recipe.models import *


def populate():

     users = {"user1":{"username":"AdamSmith","email":"ASmith@hotmail.com"   },
             "user2":{"username":"JohnBrown","email":"JohnB@hotmail.com"   },
             "user3":{"username":"GeorgeJr","email":"GeorgeJR@hotmail.com"   },
             "user4":{"username":"AndyGr","email":"AGround@hotmail.com"   },
             "user5":{"username":"Andrew","email":"A_Jack@hotmail.com"   },

            }


     # categories with recipes
     chicken = [{"id": "100",
                     "name": "Kalampoki",
                     "ingredients": " For the marinade\n1 tablespoon(s) turmeric\n1 teaspoon(s) cumin\n1 teaspoon(s) chili powder\n1 teaspoon(s) coriander, grated\n1 teaspoon(s) paprika, smoked\nsalt\n150 g strained yogurt\n500 g chicken, thigh fillet\nFor the rice\n\n250 g basmati rice\n500 g water\n2-3 tablespoon(s) olive oil\nsalt\npepper\n1 bay leaf\npeels, of 1 lemon\nFor the sauce\n\n2 tablespoon(s) olive oil\n1 onion\n2 clove(s) of garlic\n1 tablespoon(s) granulated sugar\n1 teaspoon(s) turmeric\n1 stick(s) cinnamon\n1 bay leaf\n100 g water\n200 g tomatoes, grated\n1 tablespoon(s) tomato paste\n70 g heavy cream 35%\nsalt\npepper\n1/4 bunch coriander\nTo serve\n\ncoriander",
                     "instructions": "For the marinade\n\nPreheat the oven to 180ο C (350ο F) set to fan.\nIn a bowl add the turmeric, the cumin, the chili, the coriander, the paprika, salt, pepper, and mix.\nAdd the yogurt and mix well until the ingredients are homogenized.\nCut the chicken into small pieces and add it to the bowl with the marinade. Ideally, cover it with plastic wrap and refrigerate for 2-3 hours.\nSpread the chicken into a baking pan and bake for 15 minutes.\nFor the rice\n\nPlace a pot with boiling water over low heat.\nAdd the rice, the olive oil, salt, pepper, the bay leaf, the lemon peels, and cover the pot with the lid.\nSimmer for 10-12 minutes.\nFor the sauce\n\nPlace a frying pan over high heat and add the olive oil.\nFinely chop the onion, the garlic, and add them to the pan.\nAdd the sugar, the turmeric, the cinnamon, the bay leaf, and mix.\nDeglaze the pan with the water, add the grated tomatoes, the tomato paste, and mix.\nAdd the heavy cream, salt, pepper, and simmer for 3-4 minutes.\nTransfer the chicken to the sauce, add the coriander finely chopped, and mix. Keep boiling for 1-2 minutes until the sauce thickens.\nServe the chicken with the rice and the coriander.",
                     "price": 2.13,
                     "category": "chicken",
                     "user": "AdamSmith",
                     "picture": "media/Lahmacun.jpg",
                     "portions": 3,
                     "difficulty": 2,
                     "completion_time": "15-30 minutes",
                     "calories": 489,
                     "slug":"chicken-tikka-masala"
                },


                {"id": "200",
                     "name": "Kalampoki22",
                     "ingredients": " ",
                     "instructions": " ",
                     "price": 1.52,
                     "category": "chicken",
                     "user": "JohnBrown",
                     "picture": "",
                     "portions": 4,
                     "difficulty": 3,
                     "completion_time": '30-60 minutes',
                     "calories": 356,
                }]


     categories = {"chicken":chicken}


     today = datetime.datetime.today()

     comments = {"100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ]
                
     }

     # create users
     for user,user_info in users.items():
          user = User.objects.get_or_create(username=user_info['username'],email=user_info['email'])[0]
          userProfile = UserProfile.objects.get_or_create(user1 = user,)[0]
          
          user.set_password(user.username)
          userProfile.save()
          user.save()

     # create the categories
     for category,recipes in categories.items():
          cat = add_category(category)
          # create the recipes
          for rec in recipes:
               current_user = User.objects.get(username = rec["user"])
               new_recipe = add_recipe(rec['id'],rec['name'],rec['picture'],rec['ingredients'],rec['instructions'],rec['portions'],rec['difficulty'],rec['completion_time'],rec['calories'],rec['price'],cat,current_user)
               # create the comments
               if rec["id"] in comments:
                    for comment in comments[rec["id"]]:
                         comment_user = User.objects.get(username = comment['owner'])
                         new_comment = add_comment(comment['date'],comment['recommentations'],comment_user,new_recipe)

     for category in Category.objects.all():
          for recipe in Recipe.objects.filter(category_id = category):
               print("-{}-{}".format(category.name,recipe.name))
     



     




def add_comment(date,recommentation,owner,recipe):
     category = Comment.objects.get_or_create(date=date,recommentations=recommentation,owner_id=owner,recipe_id=recipe)[0]
     category.save()
     return category


def add_recipe(id,name,picture,ingredients,instructions,portions,difficulty,time,calories,price,category,owner):
     recipe = Recipe.objects.get_or_create(id=id,name=name,picture=picture,ingredients=ingredients,instuction=instructions,portions=portions,difficulty=difficulty,completion_time=time,calories=calories,average_overall_price=price,category_id=category,owner_id=owner)[0]
     recipe.save()
     return recipe


def add_category(name):
     category = Category.objects.get_or_create(name=name)[0]
     category.save()
     return category

if __name__ == '__main__':
    print("Starting readyRecipe population script :)")
    populate()

