import os
import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE','readyRecipe.settings')


import django
django.setup()
from ready_recipe.models import *


def populate():

     # users
     users = {"user1":{"username":"AdamSmith","email":"ASmith@hotmail.com"},
              "user2":{"username":"JohnBrown","email":"JohnB@hotmail.com"},
              "user3":{"username":"GeorgeJr","email":"GeorgeJR@hotmail.com"},
              "user4":{"username":"AndyGr","email":"AGround@hotmail.com"},
              "user5":{"username":"Andrew","email":"A_Jack@hotmail.com"},
            }


     # categories with recipes
     chicken = [{"id": "110",
                 "name": "Crispy Chicken Thighs",
                 "ingredients": "200 g panko breadcrumbs\n1/2 teaspoon(s) garlic, powder\nsalt\npepper\n4 eggs, medium\n70 g buttermilk\n700 g chicken, fillets\n\nTo serve\n\n250 g vegetables, boiled\n2 tablespoon(s) olive oil\n100 g strained yogurt\n1 pinch oregano, dried",
                 "instructions": "Preheat the oven to 180ο C (350ο F) set to fan. \nLine a baking pan with parchment paper and set aside.\nIn a bowl, mix the panko breadcrumbs, the garlic, the salt, and the pepper.\nIn a second bowl, break the eggs and beat them lightly with a fork. Add the buttermilk and mix.\nDip the fillets into the egg mixture and then, bread them with the panko mixture, making sure that the fillets are completely coated.\nTransfer the breaded fillets to the baking pan and bake for 50-60 minutes, until they are golden.\nWhile the chicken is in the oven, mix the boiled vegetables and the olive oil in a bowl.\nRemove the thighs from the oven, and serve with the boiled vegetables and the yogurt. \nSprinkle with the oregano and serve.",
                 "price": 2.15,
                 "category": "Chicken and Turkey",
                 "user": "AdamSmith",
                 "picture": "Crispy-chicken-thighs.jpg",
                 "portions": 3,
                 "difficulty": 2,
                 "completion_time": '3' ,
                 "calories": 489,
                },

                {"id": "111",
                 "name": "Chicken Tikka Masala",
                 "ingredients": "For the marinade\n\n\n1 tablespoon(s) turmeric\n1 teaspoon(s) cumin\n1 teaspoon(s) chili powder\n1 teaspoon(s) coriander, grated\n1 teaspoon(s) paprika, smoked\nsalt\n150 g strained yogurt\n500 g chicken, thigh fillet\n\nFor the rice\n\n\n250 g basmati rice\n500 g water\n2-3 tablespoon(s) olive oil\nsalt\npepper\n1 bay leaf\npeels, of 1 lemon\n\nTo serve\n\n\ncoriander",
                 "instructions": "For the marinade\n\n\nPreheat the oven to 180ο C (350ο F) set to fan.\nIn a bowl add the turmeric, the cumin, the chili, the coriander, the paprika, salt, pepper, and mix.\nAdd the yogurt and mix well until the ingredients are homogenized.\nCut the chicken into small pieces and add it to the bowl with the marinade. Ideally, cover it with plastic wrap and refrigerate for 2-3 hours.\nSpread the chicken into a baking pan and bake for 15 minutes.\n\nFor the rice\n\n\nPlace a pot with boiling water over low heat.\nAdd the rice, the olive oil, salt, pepper, the bay leaf, the lemon peels, and cover the pot with the lid.\nSimmer for 10-12 minutes.",
                 "price": 1.52,
                 "category": "Chicken and Turkey",
                 "user": "JohnBrown",
                 "picture": "",
                 "portions": 4,
                 "difficulty": 3,
                 "completion_time": '3',
                 "calories": 356,
                }]

     pork = [ {"id": "112",
               "name": "Roasted Pork Loin",
               "ingredients": "For the pork loin\n\n\n2 ½ kilos pork, loin bone-in\nzest, of 2 lemons\n4 clove(s) of garlic\n1 pinch chili flakes\n5 cloves, whole\n3 tablespoon(s) olive oil\n30 g salt\npepper\n\n\nTo serve\n\n\n500 g potatoes, boiled\n3 carrots, boiled\n200 g peas, boiled\nsalt\npepper\noregano",
               "instructions": "For the pork loin\n\n\nPreheat the oven to 160°C (320° F) set to fan\nScore the pork, skin-side, vertically and diagonally.\nTransfer the pork onto a piece of parchment paper and add the lemon zest, the garlic finely chopped, the chili flakes, the cloves, olive oil, salt, pepper, and spread them over the whole surface of the pork loin.\nWrap with parchment paper, aluminum foil, and place it onto a baking pan with a rack.\nRoast for 3 hours. Uncover and roast for 30-60 more minutes.\n\n\nTo serve\n\n\nCut the potatoes and the carrots into pieces and add them to the serving plate. Add the peas, salt, and pepper.\nCut the pork into chops, along the bone.\nServe with the sauce and oregano.",
               "price": 1.52,
               "category": "Pork",
               "user": "GeorgeJr",
               "picture": "media/RoastedPorkLoin.jpg",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '4',
               "calories": 412,
               },

               {"id": "113",
               "name": "Pork Dumplings",
               "ingredients": "500 g cabbage\n1 tablespoon(s) salt\n500 g ground pork\n3 spring onions, finely chopped\n1/2 bunch coriander, fresh, finely chopped\n3 tablespoon(s) ginger, fresh, grated\n2 eggs, large, lightly beaten\n350 g rice paper wrappers\n2 tablespoon(s) olive oil\n8 tablespoon(s) water",
               "instructions": "Chop the cabbage into very thin slices.\nMix it with the salt and leave it in a colander for 15 minutes. Immediately after, press it with your hands so that it extracts its juices and then add it to a bowl.\nAdd the remaining ingredients, except for the wonton wrappers. Mix them well so that they are homogenized and prepare your dumplings.\nGet a bowl with water and line a baking pan with parchment paper.\nTake a wonton wrapper and add 1 tablespoon of the filling in the center.\nWith your fingers, lightly wet the edges all around the wrapper. Seal them easily like pouches or fold them in half and add them to the baking pan.\nPlace them into a non-stick frying pan that has a lid or into a wide non-stick pot.\nAdd 1 tablespoon sunflower oil and put half of the dumplings in. As they do not rise, you can put plenty of them in, provided that they do not touch each other.\nSauté them for 1-2 minutes until their base gets a nice golden color.\nAdd 3-4 tablespoons of water to the frying pan, lower the heat to minimum, and seal with the lid.\nSimmer for 3-5 minutes.\nRepeat the same process with the rest of the dumplings and serve.",
               "price": 3.56,
               "category": "Pork",
               "user": "AdamSmith",
               "picture": "media/pork-dumplings.jpg",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '4',
               "calories": 178,
               }
     ]

     beef = [{"id": "114",
               "name": "Sweet and sour ribeye steaks",
               "ingredients": "For the steaks\n\n\n3 kilos beef, ribeye\nsalt\npepper\n4-5 tablespoon(s) olive oil\n100 g butter\n2 clove(s) of garlic\n2-3 sprig(s) thyme\n2-3 sprig(s) rosemary\n\n\nFor the sauce\n\n\n1-2 tablespoon(s) olive oil\n1 onion\n1 clove(s) of garlic\n1 tablespoon(s) thyme\n1 teaspoon(s) butter\n200 g orange juice\n1 pinch chili flakes\n100 g balsamic cream\n400 g carrots\nsalt\npepper",
               "instructions": "For the ribeye steaks\n\n\nWith a knife, carefully separate the ribs from the ribeye and set them aside. You can season them with salt and pepper, wrap them in parchment paper and aluminum foil and bake them in the oven at 200ο C (390ο F) set to fan, for 2 ½ hours.\nPlace a large frying pan over medium heat.\nFrom the ribeye filet, cut steaks about 300 g each. You will have 9-10 steaks.\nSeason both sides with salt and pepper, drizzle with the olive oil and spread it well so that their whole surface is coated.\nPut 3 of the steaks into the frying pan. Do not overcrowd your pan so that they will be cooked properly. Cook them for 2-3 minutes on one side without mixing at all.\nFlip the steaks over and cook them for 2-3 more minutes. Add 30 g of the butter, the garlic, thyme, and rosemary.\nWith a spoon, pour the aromatic butter over the steaks for 1-2 minutes. Remove and set aside.\nFollow the same process for all of the steaks, adding extra butter.\n\n\nFor the sauce\n\n\nCut the carrots lengthwise in half, and set them aside.\nPlace a frying pan over high heat and add the olive oil.\nFinely chop the onion, the garlic and add them to the frying pan.\nAdd thyme, the butter and sauté for 1-2 minutes until the onion is caramelized.\nDeglaze the pan with the orange juice and add the chili flakes, the balsamic cream, and mix.\nAdd the carrots, salt, pepper, and simmer at low heat for 3-4 minutes until the carrots are tender.",
               "price": 4.85,
               "category": "Beef",
               "user": "GeorgeJr",
               "picture": "media/SweetAndSourRibeyeSteaks.jpg",
               "portions": 2,
               "difficulty": 1,
               "completion_time": '1',
               "calories": 587,
               },
               
               {"id": "115",
               "name": "Chili Con Carne",
               "ingredients": "2-3 tablespoon(s) olive oil\n1 onion\n2 clove(s) of garlic\n1 red bell pepper\n2 pinches granulated sugar\nsalt\npepper\nthyme\n2 tablespoon(s) tomato paste\n1 teaspoon(s) oregano, dry\n1 teaspoon(s) cumin\n1 teaspoon(s) paprika, sweet\n1 teaspoon(s) pepper, red\n100 g water\n500 g ground beef\n1 beef bouillon cube\n400 g red beans, canned\n200 g cheddar, grated\n\n\nTo serve\n\n\nnachos\nstrained yogurt\n1/2 bunch coriander\nsweet chili sauce",
               "instructions": "Place a non-stick pan over high heat. Heat 2-3 tablespoons olive oil.\nCut the onion and garlic into thin slices. Place them in the pan and mix. Add the sugar and allow 2-3 minutes until caramelized.\nCut the red pepper into small cubes and add them to the pan.\nAdd the chili flakes, oregano, cumin, paprika and sauté for 2-3 minutes.\nAdd the ground beef and mix with a wooden spoon until golden.\nAdd the tomato paste and mix until homogenized.\nAdd the red beans, beef bouillon cube, salt, pepper, water and mix for 1-2 minutes until combined.\nRemove from heat and add half of the coriander, half of the cheese and mix.\nServe along with nachos, the rest of the cheddar, the rest of the coriander, the yogurt and the sweet chili sauce.",
               "price": 4.15,
               "category": "Beef",
               "user": "JohnBrown",
               "picture": "media/ChiliConCarne.jpeg",
               "portions": 4,
               "difficulty": 2,
               "completion_time": '3',
               "calories": 687,
               },
     ]

     lamb = [{"id": "116",
               "name": "Lahmacun",
               "ingredients": "For the Lahmacun\n\n\n160 g milk, at room temperature\n80 g water, at room temperature\n1 tablespoon(s) yeast\n1 teaspoon(s) granulated sugar\n1 tablespoon(s) thyme\n350 g hard flour\nsalt\n3 tablespoon(s) olive oil\n\n\nFor the filling\n\n\n2 tablespoon(s) olive oil\n1 onion\n2 clove(s) of garlic\nsalt\npepper\n400 g ground lamb\n1/2 teaspoon(s) cumin\n1/2 teaspoon(s) fenugreek\n1 teaspoon(s) paprika, smoked\n1/2 teaspoon(s) chili flakes\n400 g canned tomatoes\n200 g gruyere cheese, grated\n\n\nTo serve\n\n\ncoriander\n1 teaspoon(s) olive oil",
               "instructions": "For the lahmatzoun\n\n\nIn a mixer’s bowl add the milk, the water, the yeast, the sugar, the thyme, and whisk well using a hand whisk. You should let the mixture sit for 5-10 minutes so that the yeast is activated.\nAdd the flour, salt, and beat with the hook attachment at medium speed for 5-8 minutes until there is a soft and elastic dough.\nPut the dough into a floured bowl, cover it with plastic wrap, and allow about 1 hour for the dough to double in volume.\nCut the dough into 6 pieces and with a rolling pin, roll it out until it has a 20 cm diameter.\nPlace a 26 cm frying pan over medium-high heat.\nSpread 1 teaspoon of the olive oil and add one of the dough pieces. Cook for 2-3 minutes on each side and set aside.\nFollow the same process for the remaining dough pieces, by adding 1 teaspoon olive oil. Set aside.\n\n\nFor the filling\n\n\nPlace the frying pan on heat again and add 2 tablespoons olive oil.\nFinely chop the onion, the garlic, and add them to the pan. Season with salt, pepper, and sauté until they are caramelized.\nAdd the ground meat and sauté until golden brown.\nAdd the cumin, the fenugreek, the paprika, the chili flakes, and mix.\nAdd the canned tomatoes, salt, pepper, and simmer at medium heat for 5-7 minutes until the moisture evaporates.\nSet aside to cool.\n\n\nTo assemble\n\n\nPreheat the oven, set to grill.\nPut the lahmatzouns into baking pans lined with parchment paper and divide the ground meat. Spread with a spoon so that their whole surface is covered.\nSprinkle with the gruyere cheese and bake for 8-10 minutes until golden.\nServe with coriander and olive oil.",
               "price": 3.85,
               "category": "Lamb",
               "user": "AdamSmith",
               "picture": "media/Lahmacun.jpg",
               "portions": 3,
               "difficulty": 5,
               "completion_time": '3',
               "calories": 525,
               },
               
               {"id": "117",
               "name": "Roast leg of lamb fillet",
               "ingredients": "For the marinade\n\n\n2 teaspoon(s) thyme, fresh leaves, finely chopped\n2 teaspoon(s) rosemary, fresh leaves, finely chopped\n3 clove(s) of garlic, finely chopped\n1 onion, medium, finely chopped\n80 g olive oil\n70 g vinegar, of red wine\njuice, of 1/2 orange\n3 tablespoon(s) mustard, dijon\n\nFor the meat\n\n\n2 kilos lamb, leg, boneless, butterflied\n1 teaspoon(s) salt\n1/2 teaspoon(s) pepper\nmashed potatoes , to serve",
               "instructions": "In a large bowl, add the marinade ingredients and mix well.\nAdd the meat inside, mix, cover with plastic wrap, and place the bowl in the refrigerator for 24 hours.\nDuring this time, mix well 2-3 times.\nThe following day, preheat the oven to 180°C (356° F), set to fan.\nRemove the meat from the marinade and place it onto a baking pan.\nSeason with salt and pepper, and roast it for about 70 minutes.\nRemove the baking pan from the oven and keep the juices with which, if you want, you can make a reduction sauce in a frying pan.\nCut the meat into portions and serve it with the mashed potatoes and some of the juice.",
               "price": 3.75,
               "category": "Lamb",
               "user": "JohnBrown",
               "picture": "media/lambFillet.jpg",
               "portions": 5,
               "difficulty": 3,
               "completion_time": '4',
               "calories": 560,
               },
     ]

     rice_potatoes = [{"id": "118",
                       "name": "Fried wild rice",
                       "ingredients": "200 g wild rice\n1 liter water\n1 vegetable bouillon cube\n2 tablespoon(s) olive oil\n100 g portobello mushrooms\n8 carrots, baby\n1 onion\n1 clove(s) of garlic\n50 g soy sauce\n2 spring onions\npepper\n1 tablespoon(s) sesame seeds, to serve",
                       "instructions": "Place the rice, water and vegetable bouillon cube in a pot over medium heat.\nSimmer for 40 minutes until the rice softens.\nStrain and set aside to cool.\nHeat the olive oil in a wok.\nCut the mushrooms into slices 1 cm thick. Sauté until softened.\nAdd the carrots (whole).\nFinely chop the onion. Cut the garlic into thin slices.\nAdd them to the wok with the mushrooms and sauté for 2-3 minutes until slightly golden.\nAdd soy sauce. Add wild rice and mix with a wooden spoon.\nFinely chop the spring onions. Add them to the pan and mix.\nRemove pan from heat. Serve while warm with pepper and sesame.",
                       "price": 0.85,
                       "category": "Rice and Potatoes",
                       "user": "AndyGr",
                       "picture": "media/FriedWildRice.jpg",
                       "portions": 3,
                       "difficulty": 1,
                       "completion_time": '1',
                       "calories": 146,
                      },
                      
                      {"id": "119",
                       "name": "Mashed Potatoes",
                       "ingredients": "1 kilo potatoes\n75 g butter\nsalt\npepper",
                       "instructions": "Preheat oven to 180°C (390° F) Fan.\nSpread a generous amount of coarse salt in to a small baking pan.\nAdd the potatoes and prick them with a fork. This will allow a lot of the moisture to escape.\nBake for 45 minutes to 1 hour.\nWhen ready, remove them from the oven.\nCut them half and immediately scoop out the flesh with a spoon.\nPlace the potatoes on to a flat sieve with a paper towel placed underneath it (you can also use a potato masher).\nPress them through the sieve with the aid of a scraper. Never use a processor to make mashed potatoes because they will turn out gummy.\nPlace a pan over low heat.\nAdd the potatoes and the butter in the pan.\nStir with a spatula, giving the potatoes time to soak up all of the butter and become smooth and creamy. No milk or heavy cream is required.\nRemove from heat and season with salt and freshly ground pepper.\nAdd a knob of butter and season with salt and freshly ground pepper.",
                       "price": 0.60,
                       "category": "Rice and Potatoes",
                       "user": "AdamSmith",
                       "picture": "media/MashedPotatoes.jpg",
                       "portions": 3,
                       "difficulty": 1,
                       "completion_time": '1',
                       "calories": 176,
                      },         
     ]

     salads = [{"id": "120",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "AndyGr",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },      
               
               {"id": "121",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "GeorgeJr",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },
     ]

     soups = [{"id": "122",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "AdamSmith",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },      
               
               {"id": "123",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "GeorgeJr",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },
     ]

     pasta = [ {"id": "124",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "AndyGr",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },
               
               {"id": "125",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "Andrew",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },
     ]

     vegan = [ {"id": "126",
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
               },

               {"id": "127",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "GeorgeJr",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               }
     ]

     vegetarian =[{"id": "128",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "Andrew",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },
               
               {"id": "129",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "AndyGr",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },
     ]

     diet = [ {"id": "130",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "Andrew",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },
               
               {"id": "131",
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
               },
     ]

     christmas = [{"id": "132",
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
               },
               
               {"id": "133",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "AndyGr",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },
     ]

     desserts = [{"id": "134",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "Andrew",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },      
               
               {"id": "135",
               "name": "Kalampoki22",
               "ingredients": " ",
               "instructions": " ",
               "price": 1.52,
               "category": "chicken",
               "user": "AndyGr",
               "picture": "",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '30-60 minutes',
               "calories": 356,
               },
     ]

     


     categories = {"Chicken and Turkey":chicken,
                   "Beef":beef,
                   "Pork":pork,
                   "Lamb":lamb,
                   "Rice and Potatoes":rice_potatoes,
                   "Salad":salads,
                   "Soups":soups,
                   "Pasta":pasta,
                   "Vegan":vegan,
                   "Vegetarian":vegetarian,
                   "Diet":diet,
                   "Christmas Recipes":christmas,
                   "Desserts":desserts,
     }



     today = datetime.datetime.today()


     # comments
     comments = {"100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                         ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"date":today,"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"date":today,"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "100": [{"date":today,"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
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

     # display all the recipes with their category
     for category in Category.objects.all():
          for recipe in Recipe.objects.filter(category_id = category):
               print("-{}-{}".format(category.name,recipe.name))
     




# helper function to save comments
def add_comment(date,recommentation,owner,recipe):
     category = Comment.objects.get_or_create(date=date,recommentations=recommentation,owner_id=owner,recipe_id=recipe)[0]
     category.save()
     return category

# helper function to save the recipes
def add_recipe(id,name,picture,ingredients,instructions,portions,difficulty,time,calories,price,category,owner):
     recipe = Recipe.objects.get_or_create(id=id,name=name,picture=picture,ingredients=ingredients,instuction=instructions,portions=portions,difficulty=difficulty,completion_time=time,calories=calories,average_overall_price=price,category_id=category,owner_id=owner)[0]
     recipe.save()
     return recipe

# helper function to save the categories
def add_category(name):
     category = Category.objects.get_or_create(name=name)[0]
     category.save()
     return category


if __name__ == '__main__':
    print("Starting readyRecipe population script :)")
    populate()

