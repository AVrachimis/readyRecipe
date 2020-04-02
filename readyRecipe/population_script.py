# -*- coding: utf-8 -*- 
import os
import random


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
                 "picture": "ChickenTikkaMasala.jpg",
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
               "name": "Caesar Salad with Chicken",
               "ingredients": "2 lemons\n3 sprig(s) rosemary\n3 sprig(s) thyme\n1 onion\n1 1/2 chicken, breast\n100 g cherry tomatoes\n100 g hazelnuts\n\nFor the Caesar dressing\n\n\n300 g strained yogurt\n1 lemon\n2 tablespoon(s) olive oil\n1 onion, small, finely chopped\nsalt\npepper\n4 salt-cured anchovies, fillets",
               "instructions": "Fill a pot half way with water.\nPlace over medium to high heat and bring to a boil.\nSlice the lemons and add them to the pot.\nAdd the rosemary and thyme.\nQuarter the onion and add it to the pot.\nLast, add the chicken and boil for 20 minutes.\nWhen the chicken reaches 65* C (149* F) and is no longer pink, remove from pot and set aside to cool.\nChop into 1-2 cm pieces and set aside.\nTo prepare the kale, remove the thick, hard stems from the leaves with a knife.\nCut the leaves into 4 pieces and transfer to a bowl.\nPrepare the dressing in a separate bowl.\nAdd the yogurt, the juice from 1 lemon, olive oil, onion, salt and pepper.\nWhisk until completely combined.\nFinely chop the anchovy fillets and add them to the bowl.\nStir well and add the dressing to the salad.\nToss to distribute the dressing evenly.\nAdd the pieces of boiled chicken and cherry tomatoes (cut in half).\nCoarsely chop the hazelnuts with a knife and add them to the bowl.\nSeason to taste and serve.",
               "price": 1.92,
               "category": "Salad",
               "user": "AndyGr",
               "picture": "media/CaesarSaladWithBoiledChicken.jpg",
               "portions": 1,
               "difficulty": 2,
               "completion_time": '1',
               "calories": 436,
               },      
               
               {"id": "121",
               "name": "Tuna salad with guacamole",
               "ingredients": "For the guacamole\n\n\n1 avocado(s), ripe\n50 g water\n2 tablespoon(s) juice, lime\nzest, of 1 lime\n1 spring onion, finely chopped\n1 chili pepper, small\n1/2 clove(s) of garlic, minced\n1 pinch curry, powder\nsalt\npepper\n\nFor the tuna salad\n\n\n200 g melon, cut in to 1-2 cm cubes\n340 g tuna, in water, canned\n1 lettuce, roughly chopped\n1 red bell pepper, sliced\n50 g walnuts, roughly chopped",
               "instructions": "For the guacamole\n\n\nPrepare the avocado. Remove the peel from the avocado and chop.\nBeat the avocado and the rest of the ingredients in a blender, until you create a soft mixture. If you want a thinner mixture add a little more water.\nRefrigerate the guacamole until you prepare the salad.\n\nFor the tuna salad\n\n\nCombine all of the ingredients in a bowl.\nAdd the guacamole, mix and serve.",
               "price": 2.13,
               "category": "Salad",
               "user": "GeorgeJr",
               "picture": "media/TunaSaladWithGuacamole.jpg",
               "portions": 2,
               "difficulty": 1,
               "completion_time": '1',
               "calories": 279,
               },
     ]

     soups = [{"id": "122",
               "name": "Carrot soup",
               "ingredients": "2 leeks\n2 tablespoon(s) olive oil\n2 onions, dry\n6 carrots, large\n1 clove(s) of garlic\n1 tablespoon(s) granulated sugar\n100 g white wine\njuice, of 1 lemon\n1/2 teaspoon(s) coriander\n1/2 teaspoon(s) cumin\n1 pinch nutmeg\n1 level tablespoon(s) turmeric\n2 liters water, boiling\n2 vegetable bouillon cubes\n100 g heavy cream 35%\njuice, of 1 lime\nsalt\npepper\n\nTo serve\n\n\n2 slices lime(s)\ncoriander, fresh\nolive oil\nolive bread",
               "instructions": "In a pot, add the olive oil, coarsely chopped leeks and coarsely chopped onions. Sauté.\nAdd the coarsely chopped carrots, finely chopped garlic and granulated sugar. Sauté for 7-8 minutes.\nDeglaze with white wine and the juice from 1 lemon.\nAdd the coriander, cumin, nutmeg, turmeric, 1 ½ liter water and vegetable cubes.\nWhen the mixture comes to a boil, lower heat and simmer for 30 minutes.\nRemove soup from heat and beat with an immersion blender until smooth and creamy.\nAdd the heavy cream, 500 g boiling water, juice from 1 lime, salt and pepper. Beat again.\nServe with lime wedges, fresh coriander, olive oil and olive bread.",
               "price": 0.92,
               "category": "Soups",
               "user": "AdamSmith",
               "picture": "media/CarrotSoup.jpg",
               "portions": 2,
               "difficulty": 2,
               "completion_time": '2',
               "calories": 153,
               },      
               
               {"id": "123",
               "name": "Beef soup",
               "ingredients": "1 kilo beef, shank\nsalt\npepper\n50 g all-purpose flour\n2 tablespoon(s) olive oil\n2 clove(s) of garlic\n2 bay leaves\n2 sprig(s) rosemary\njuice, of 1 lemon\npeels, of 1 lemon\n50 g white wine\n1 1/2 liter water\n1 kilo vegetable soup mix\n1/2 bunch celery leaves, only the leaves\n\nTo serve\n\n\nslices lemon\n1 tablespoon(s) celery leaves, only the leaves\n1 tablespoon(s) olive oil\npepper",
               "instructions": "Place a pot over high heat and let it get very hot.\nCut the beef into small pieces.\nSeason with salt and pepper. Dust with flour and mix with your hands to coat.\nAdd 2 tablespoons olive oil to the pot and add the pieces of meat.\nSauté until golden.\nAdd the garlic, the bay leaves, rosemary and lemon peels.\nAdd the wine and lemon juice.\nAs soon as the wine evaporates, add the water, cover with lid and boil for 1 ½ hours.\nAdd the vegetables and celery leaves.\nCover with lid and simmer for 20-30 minutes.\nServe with lemon wedges, celery leaves, olive oil and freshly ground pepper.",
               "price": 3.41,
               "category": "Soups",
               "user": "GeorgeJr",
               "picture": "media/VegetableBeefSoup.jpg",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '3',
               "calories": 417,
               },
     ]

     pasta = [ {"id": "124",
               "name": "Linguine with Broccoli Pesto",
               "ingredients": "150 g broccoli\n10 salt-cured anchovies, drained\n1 clove(s) of garlic\n10 mint leaves\n2 tablespoon(s) parmesan cheese\nsalt\npepper\n120 ml olive oil\n40 g hazelnuts, blanched\nzest, of 1 lemon\njuice, of 1 lemon\n300 g linguine\nsalt",
               "instructions": "Cut the broccoli into florets and boil in a pot of salted boiling water for 1 minute.\nRemove from pot with a slotted spoon and transfer to a bowl full of chilled water and allow to cool for a few minutes.\nDrain broccoli, pat dry and set aside.\nPlace a separate pot full of salted water over high heat and bring to a boil. Add the linguine and cook for 7-8 minutes or for 1 minute less than the instructions on the package.\nWhile the pasta is boiling, prepare the pesto.\nBeat all of the ingredients for the pesto in a food processor until they are pureed.\nAdd the parmesan and beat to combine.\nTaste the pesto and adjust according to your taste.\nBeat again. If the pesto is too thick, add a little more olive oil.\nWhen the pasta is ready, reserve 100 ml of the pasta water and drain.\nAdd the pesto to the linguine and toss.\nIf they are too dry add a little of the reserved pasta water, toss and serve",
               "price": 2.24,
               "category": "Pasta",
               "user": "AndyGr",
               "picture": "media/LinguineWithBroccoliPesto.jpeg",
               "portions": 4,
               "difficulty": 2,
               "completion_time": '2',
               "calories": 582,
               },
               
               {"id": "125",
               "name": "Spaghetti with mushroom sauce",
               "ingredients": "3-4 tablespoon(s) olive oil\n1 onion\n1 carrot\n2 leeks\n1 tablespoon(s) granulated sugar\n1 bay leaf\n1 clove(s) of garlic\n1 tablespoon(s) thyme\n1 teaspoon(s) chili flakes\nsalt\npepper\n800 g champignon mushrooms\n1 tablespoon(s) tomato paste\n80 g white wine\n150 g water, hot\n2 tomatoes\n1 vegetable bouillon cube\n500 g spaghetti, No 6\nthyme\n1 tablespoon(s) olive oil",
               "instructions": "Place a deep pan over high heat and add the olive oil.\nCoarsely chop the onion, chop the carrots into half-moon shapes, dice the leeks and add them to the pan.\nAdd the sugar, bay leaf, minced garlic, thyme, chili flakes, salt and pepper.\nSauté the vegetables for 10 minutes, until they caramelize nicely.\nChop the mushrooms in half or into four pieces and add them to the pan. Add the tomato paste and sauté for 5-8 minutes until they decrease in volume.\nAdd the wine, allow the alcohol to evaporate and then add the water.\nGrate the tomatoes with the large blades of a grater, discard the skin and add to the pan along with the bouillon cube.\nLower heat and simmer for 15 minutes.\nIn a pot full of boiling water, add the salt and spaghetti. Boil according to the directions on the package.\nWhen ready, drain the pasta and immediately transfer to the pan with the sauce. Mix for 1-2 minutes, until the sauce thickens and remove from heat.\nServe with thyme, pepper and olive oil.",
               "price": 2.15,
               "category": "Pasta",
               "user": "Andrew",
               "picture": "media/SpaghettiWithMushroomSauce.jpg",
               "portions": 3,
               "difficulty": 1,
               "completion_time": '1',
               "calories": 675,
               },
     ]

     vegan = [ {"id": "126",
               "name": "Vegan Burger",
               "ingredients": "80 g quinoa\n1 tablespoon(s) olive oil\n6 portobello mushrooms, cut into 3 mm slices\n1 tablespoon(s) coriander, seeds, grated\n1 teaspoon(s) cumin, powder\n1 1/2 teaspoon(s) ginger, powder\n1 teaspoon(s) pepper\n350 g chickpeas, boiled\n2 tablespoon(s) tahini\n2 tablespoon(s) soy sauce\n2 clove(s) of garlic\n1 teaspoon(s) cumin, seeds\n3 tablespoon(s) parsley, finely chopped\n8 apricots, dried, finely chopped\n50 g panko breadcrumbs, or dried breadcrumbs\nsalt, optionally\n6 vegan burger buns, whole wheat",
               "instructions": "Rinse the quinoa plenty of times, until the water comes out clean.\nBoil the quinoa in a saucepan with plenty of water, for 15 minutes.\nDrain it, rinse with cold water, drain it again and set it aside in a bowl, until needed.\nAdd the olive oil in a frying pan and sauté the mushrooms with the spices, until their water is evaporated and they turn golden.\nIn a food processor add the chickpeas, the tahini, the soy sauce, the garlic, and beat until they become a paste.\nPour the mixture into a bowl and add the quinoa, the mushrooms, the cumin, the parsley, the apricots, and the panko or dried breadcrumbs.\nHave a taste and check if any salt is needed since soy sauce is pretty salty.\nMix well and, by wetting your hands, shape 6 patties.\nPlace the burger patties on a baking sheet and, as soon as you wrap them with plastic wrap, refrigerate them for at least 4 hours to thicken.\nPreheat the oven to 190°C (370° F) set to fan.\nBake for 20 minutes.\nHalfway through the baking time, flip them over and continue cooking for 10 more minutes.\nServe with the burger buns, the avocado, the tomato, and the remaining accompaniments.",
               "price": 3.65,
               "category": "Vegan",
               "user": "JohnBrown",
               "picture": "media/veganBurger.jpeg",
               "portions": 6,
               "difficulty": 2,
               "completion_time": '2',
               "calories": 541,
               },

               {"id": "127",
               "name": "Vegan Chocolates",
               "ingredients": "120 g cocoa butter\n40 g olive oil\n80 g maple syrup\n100 g cocoa powder, sifted\n1 pinch salt",
               "instructions": "Finely chop the cocoa butter and add it to a heatproof bowl along with the olive oil.\nTransfer the bowl over a bain-marie and allow 1 minute for the cocoa butter to melt. \nAs soon as it melts, add the maple syrup, the cocoa powder, and the salt. \nMix with a hand whisk until there is a smooth and shiny mixture.\nPour the mixture into any silicone molds that you like and refrigerate for at least 3 hours, so that the chocolates thicken well. \nRemove them from the molds and serve right away.\nStore in the refrigerator in an airtight container for about 1 month.",
               "price": 2.41,
               "category": "Vegan",
               "user": "GeorgeJr",
               "picture": "media/Veganchocolates.jpg",
               "portions": 3,
               "difficulty": 4,
               "completion_time": '6',
               "calories": 354,
               }
     ]

     vegetarian =[{"id": "128",
               "name": "Easy Vegetarian Tacos",
               "ingredients": "2 x 400g tins beans (e.g. black beans, cannellini beans, borlotti beans), drained and rinsed\n100g/3½oz frozen peas or sweetcorn\n2 x 400g tins chopped tomatoes\n1 tsp dried oregano\n¼ tsp dried red chilli flakes\n2 tbsp tomato purée\n8 crispy tacos shells\n½ ripe avocado\n¼ lemon, juice only\nhandful coriander leaves, roughly chopped\n60g/2¼oz Cheddar cheese, grated, to serve\nsoured cream, to serve",
               "instructions": "Preheat the oven to 180ο C (350ο F) set to fan.\nTake a muffin pan and flip it over. Place half of the tortillas between the muffin cups and bake for 5-7 minutes.\nFollow the same process for the remaining ones. Let them cool.\nPlace a frying pan over high heat and add 2-3 tablespoons olive oil.\nCoarsely chop the onion, finely chop the garlic, and add them to the pan. Season with salt, pepper, and sauté for 2-3 minutes.\nAdd the lentils and sauté for 1-2 minutes. Add the turmeric, the cumin, the paprika, the cayenne pepper, and sauté.\nAdd the canned tomatoes, the vegetable stock, the cherry tomatoes cut in half, and boil at medium-low heat for 30-35 minutes.\nnRemove and let it cool.\nAdd the coriander finely chopped, and mix. Divide the filling among the tortillas, add the yogurt, the coriander, and the paprika.\nServe with rocket leaves and olive oil.",
               "price": 3.58,
               "category": "Vegetarian",
               "user": "Andrew",
               "picture": "media/easy_vegetarian_tacos_88736_16x9.jpg",
               "portions": 4,
               "difficulty": 3,
               "completion_time": '3',
               "calories": 298,
               },
               
               {"id": "129",
               "name": "Vegetarian Ravioli",
               "ingredients": "For the homemade pasta dough\n\n\n250 g all-purpose flour, + extra for dusting\n3 eggs, medium\n2 tablespoon(s) olive oil\n1 teaspoon(s) salt\n\n\nFor the stuffing\n\n\n60 g olive oil\n400 g asparagus, washed and cleaned\n3 spring onions, finely chopped\n60 g water\n1/2 teaspoon(s) salt\n1/2 teaspoon(s) pepper, + extra to serve\n2 pinches cayenne pepper\n50 g pecorino cheese, grated\n150 g ricotta\n1 egg\nmint, fresh, finely chopped to serve\n\n\nFor the ravioli\n\n\nall-purpose flour, for rolling out the dough\n1 egg yolk, diluted in 1 tablespoon water, for sealing the dough\nsalt\n2 tablespoon(s) butter\n1 tablespoon(s) olive oil",
               "instructions": "For the homemade pasta dough\n\n\nPlace the flour on your working surface and make a well in its center. Add in the eggs, lightly beaten, the olive oil, and the salt.\nMix with a fork, incorporating a little flour at a time. When the dough starts forming and you aren’t able to continue mixing with the fork, start kneading with your hands.\nFirstly, the dough will stick to your fingers but if you knead it constantly for at least 10 minutes, you will see it thickening and getting the desired consistency. If you want, you can make the dough in the mixer, too.\nWhen it’s ready (it will have a velvety texture and it won’t stick to your hands anymore), wrap it in plastic wrap so that it doesn’t dry, and let it rest for 30-60 minutes.\n\nFor the stuffing\n\n\nIn a frying pan over medium heat, add half of the olive oil. Add half of the asparagus cut into 3 pieces, half of the spring onions, and sauté them for 3 minutes.\nAdd 60 g water, lower the heat, and cover the pan with a lid.\nSimmer for 6-8 minutes, depending on the size of the asparagus, checking regularly that the water is not evaporated.\nAs soon as the asparagus is completely boiled, remove it from the frying pan, add into a bowl and let it cool.\nThen, in the bowl with the asparagus, add the remaining ingredients for the stuffing, and mix well.\nSet it aside until needed.\n\nFor the ravioli\n\n\nCut the dough into four pieces.\nShape one of the pieces into a strip.\nDust your working surface with flour, place the strip, and lightly press it with your fingers.\nAdd flour and roll out the dough with a rolling pin, until you get a very thin and wide sheet.\nCut its edges with a knife to straighten all the sides.\nFold it in half and set it aside, covering it with a tea towel so that it doesn’t dry. Follow the same process for the remaining dough pieces.\nSpread one of the sheets on your working surface.\nUse a spoon to take a little of the stuffing and place it over half of the dough, leaving a 2 cm gap between each spoonful of stuffing.\nWith a pastry brush, spread the egg wash over the dough, around the stuffing.\nCover the stuffing with the other “half” of the empty dough (like folding it).\nLightly press the filling, so that there is no air left inside, and then press the dough well to stick together.\nWith a round 4-5 cm cookie cutter, cut the ravioli into round pieces. At this point, if you don’t want to cook them right away, add them to a baking pan lined with parchment paper, cover with plastic wrap, and put it in the freezer where you can store them for 1 month.\nPlace a pot with water over medium heat.\nAs soon as the water starts boiling, add salt and the ravioli.\nAs soon as they start rising to the surface (in about 2-3 minutes), they are ready; so, remove them from the pot and drain. Put aside 80 g of the water where the ravioli boiled for the sauce.\nAdd the remaining asparagus to the pan -cut into 3 pieces- along with the rest of the spring onions, the olive oil, and the butter.\nSauté for 2 minutes, add the 80 g of water that you put aside, and simmer for 2 minutes.\nAdd the boiled and drained ravioli into the pan with the butter, the olive oil, and sauté them for a few minutes.\nServe the ravioli warm, sprinkling them with a little finely chopped mint and pepper.",
               "price": 2.54,
               "category": "Vegetarian",
               "user": "AndyGr",
               "picture": "media/VegetarianRavioli.jpg",
               "portions": 2,
               "difficulty": 5,
               "completion_time": '4',
               "calories": 341,
               },
     ]

     diet = [ {"id": "130",
               "name": "Fish And Spinach Masala",
               "ingredients": "4 salmon steaks (skinned, each weighing 115–175g, 4–6oz)\n350 grams brown rice\n2 garlic cloves (crushed)\n1 teaspoon chilli sauce\n2 teaspoons garam masala\n2 tablespoons Flora Cuisine (or 25g Flora Buttery)\n4 spring onions (finely chopped)\n1 teaspoon turmeric\n400 grams chopped tomatoes (can)\nchilli sauce (to taste)\n175 grams fresh spinach leaves\nblack pepper",
               "instructions": "Mix together the paste ingredients and spread over the fish steaks. Cover and chill for about 2 hours.\nPlace the fish in an ovenproof dish, cover and bake in a preheated oven at 180°C, 160°C fan, gas mark 4 for 15–20 minutes or until cooked.\nMeanwhile, to make the sauce, place all ingredients except the spinach in a saucepan and bring to the boil, stirring. Simmer gently for 5 minutes, stirring occasionally. Stir in the spinach, bring to the boil and simmer gently for about 3–4 minutes.\nCook the rice following packet instructions and drain.\nServe the fish on the sauce with the rice.",
               "price": 4.58,
               "category": "Diet",
               "user": "Andrew",
               "picture": "media/FishAndSpinachMasala.jpg",
               "portions": 1,
               "difficulty": 2,
               "completion_time": '1',
               "calories": 296,
               },
               
               {"id": "131",
               "name": "Chickpea Salad",
               "ingredients": "For the sauce\n\n160 g strained yogurt\n2 tablespoon(s) apple cider vinegar\n1 teaspoon(s) mustard\n1 teaspoon(s) honey\n1/2 teaspoon(s) salt\n1/4 teaspoon(s) pepper\n1/2 teaspoon(s) chili flakes\n\nFor the salad\n\n\n400 g chickpeas, boiled\n2 stick(s) celery, peeled and finely chopped\n1 apple, cut into thin slices\n140 g grape, red, seedless and cut in half\n1 onion, finely chopped\n70 g walnuts, finely chopped\n200 g spinach, baby\nparsley, finely chopped + extra to serve",
               "instructions": "Prepare the sauce for the salad by mixing the yogurt, the apple cider vinegar, the mustard, the honey, the salt, the pepper, and the chili flakes in a bowl with a spoon. \nIn another large bowl, mix all the other ingredients for the salad.\nServe the salad garnished with the sauce and sprinkle with finely chopped parsley.\nAlternatively, pour the sauce that you prepared over the salad, and mix all the ingredients together very well. \nRefrigerate the bowl, so that it chills well. \nYou can store the salad in the refrigerator, for up to 3 days.",
               "price": 1.42,
               "category": "Diet",
               "user": "JohnBrown",
               "picture": "media/ChickpeaSalad.png",
               "portions": 6,
               "difficulty": 1,
               "completion_time": '1',
               "calories": 250,
               },
     ]

     christmas = [{"id": "132",
               "name": "Stuffed Roast Turkey Breast",
               "ingredients": "For the filling\n\n\n30 g butter\n1 tablespoon(s) olive oil\n2 onions\n1 clove(s) of garlic\nsalt\npepper\n1 teaspoon(s) thyme\n1 pinch chili flakes\n50 g sandwich bread , grated\n6-7 sage leaves\n1 pinch granulated sugar\n150 g chestnuts, boiled\nzest, of 1 lemon\n\nFor the turkey\n\n\n1200 g turkey\nsalt\npepper\n250 g bacon\n1 tablespoon(s) butter",
               "instructions": "For the stuffing\n\nPlace a deep frying pan on heat, and add the butter and the olive oil.\nCoarsely chop the onions and add them to the pan.\nFinely chop the garlic and add it to the pan.\nAdd salt, pepper, the thyme, the chili flakes, the bread, and mix.\nAdd the sage finely chopped, the sugar, the chestnuts into pieces, and sauté for 1-2 minutes.\nRemove from the heat and add the lemon zest. Set aside to cool.\n\nFor the turkey\n\nPreheat the oven to 180ο C (350ο F) set to fan.\nSpread a piece of aluminum foil and parchment paper onto your working surface. Add salt, pepper, and place 6 pieces of kitchen twine.\nSpread half of the bacon rashers, add salt, pepper, half of the butter, and place the turkey breast over them.\nCut the fillet in half, lengthways, in order to create a pocket. Add the stuffing and seal the fillet.\nWrap with the remaining bacon, season with salt and pepper, add the remaining butter, and tie well with the kitchen twine.\nWrap with the parchment paper and aluminum foil, and transfer to a baking pan with a rack.\nRoast for 1 ½ hours covered. Then, uncover and roast for 10-15 more minutes.",
               "price": 4.82,
               "category": "Christmas Recipes",
               "user": "JohnBrown",
               "picture": "media/StuffedRoastTurkeyBreast.jfif",
               "portions": 6,
               "difficulty": 3,
               "completion_time": '4',
               "calories": 566,
               },
     ]

     desserts = [{"id": "134",
               "name": "Pancakes with fruits",
               "ingredients": "200 g strained yogurt\n1 egg\n3 tablespoon(s) seed oil\n20 g granulated sugar\n1 teaspoon(s) vanilla extract\n90 g all-purpose flour\n1/2 teaspoon(s) baking soda\n1 teaspoon(s) baking powder\n1 pinch salt\nseed oil, for frying\n4 tablespoon(s) blueberries\n2 tablespoon(s) blackberries\n4 strawberries\n1 banana\nedible flowers",
               "instructions": "Combine the yogurt, egg, vegetable oil, sugar and vanilla extract in a bowl, using a fork until completely combined. You should have a fluid mixture.\nIn a separate bowl, add the flour, baking soda, baking powder and salt. Mix with a fork to combine.\nPlace a nonstick pan over medium heat and let it get very hot.\nIn order to cook the pancakes you need a very small amount of vegetable oil. In order to make sure you have the right amount of oil you will need a potato. Cut the potato in half, pick it up with a fork and dip the cut side into the oil and brush the pan with it.\nUsing a tablespoon, pick up a spoonful of the pancake batter and add it to the hot pan.\nYou can add up to 3 spoonfuls, making sure to leave enough space between them since they will spread while cooking and you don’t want them sticking together.\nOver the first pancake, add 1 tablespoon of blueberry and 1 thinly sliced strawberry.\nOver the 2nd pancake, add 1 tablespoon blackberries and 1 thinly sliced strawberry.\nOver the 3rd pancake add 1 thinly sliced banana.\nYou can create any other combination you like.\nCook for 2-3 minutes, until golden without moving them.\nTo make sure they are ready, lift the edge of one pancake with a spoon.\nFlip them over and cook for another 2-3 minutes, until golden.\nRepeat the same process until all of the pancake batter is finished.\nTo serve, place a pancake on a serving dish, drizzle with honey and top with fresh fruit. Cover with another pancake, drizzle with honey and top with fresh fruit.\nRepeat the same process until all of the pancakes are finished.\nYou can also add some lovely edible flowers.",
               "price": 3.61,
               "category": "Desserts",
               "user": "Andrew",
               "picture": "media/pancakeWithFruits.jpg",
               "portions": 1,
               "difficulty": 1,
               "completion_time": '2',
               "calories": 752,
               },      
               
               {"id": "135",
               "name": "Tofu strawberry mousse",
               "ingredients": "400 g strawberries, fresh or frozen\n200 g tofu, soft\n50 g honey\n1/4 teaspoon(s) vanilla extract\n1 teaspoon(s) chia seeds\n100 g coconut milk\n50 g blueberries, to serve\n50 g strawberries, fresh or frozen, to serve\nicing sugar, to serve, optionally",
               "instructions": "In a food processor, beat all of the ingredients until the strawberries and tofu are dissolved and there is a smooth mousse.\nDivide the mousse into glasses and refrigerate for 30-40 minutes, to thicken.\nServe with the blueberries, strawberries, and icing sugar.",
               "price": 1.18,
               "category": "Desserts",
               "user": "AndyGr",
               "picture": "media/TofuStrawberryMousse.jpg",
               "portions": 3,
               "difficulty": 1,
               "completion_time": '3',
               "calories": 95,
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





     # comments
     comments = {"110": [{"recommentations":"Really nice recipe, Congratulations","owner":"AndyGr"},
                         {"recommentations":"I didn’t have any bread. It turned out terrible.","owner":"AdamSmith"},
                         {"recommentations":"Any recommendations to reduce the calories of the meal?","owner":"GeorgeJr"},
                        ],
               "111": [{"recommentations":"Really nice recipe, except of the sauce at the top.","owner":"AndyGr"},
                         {"recommentations":"TOO SPICY!! I dont recommend it...","owner":"Andrew"},
                         {"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"GeorgeJr"},
                         ],
               "112": [{"recommentations":"Really nice and juicy pork recipe!!","owner":"AndyGr"},
                         {"recommentations":"Can I cook the pork medium-rare?","owner":"AdamSmith"},
                         {"recommentations":"No.....","owner":"GeorgeJr"},
                        ],
               "113": [{"recommentations":"Almost Perfect","owner":"AndyGr"},
                         {"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"recommentations":"I cooked it a little bit longer, and it was surprisingly delicious!","owner":"GeorgeJr"},
                        ],
               "114": [{"recommentations":"Perfect medium rare steak","owner":"AndyGr"},
                         {"recommentations":"The sauce is too sweet. Stronlgy recommend it without any sauce!!","owner":"Andrew"},
                         {"recommentations":"I cooked it a little bit longer but the taste it was still nice!","owner":"GeorgeJr"},
                        ],
               "115": [{"recommentations":"It could be better","owner":"AndyGr"},
                         {"recommentations":"Really uncommon taste, not sure if I like it or not.","owner":"AdamSmith"},
                        ],
               "116": [{"recommentations":"Too many spices!!","owner":"AdamSmith"},
                         {"recommentations":"Just Perfect","owner":"Andrew"},
                         {"recommentations":"I cooked it a little bit longer, added 3 tbsp red curry paste and it was surprisingly delicious!","owner":"JohnBrown"},
                        ],
               "117": [{"recommentations":"Nice and juicy!!","owner":"AndyGr"},
                         {"recommentations":"Perfect texture..","owner":"AdamSmith"},
                         {"recommentations":"I cooked it a little bit longer, byt it was still delicious.","owner":"GeorgeJr"},
                        ],
               "118": [{"recommentations":"Simple and quick rice recipe","owner":"AdamSmith"},
                        ],
               "120": [{"recommentations":"Nice, but I perfect with avocados and fried chicken!!","owner":"AndyGr"},
                         {"recommentations":"Really tasty and easy to make","owner":"Andrew"},
                        ],
               "122": [{"recommentations":"Really nice recipe, Congratulations","owner":"JohnBrown"},
                         {"recommentations":"Good texture and taste, i added some more pepper to make it better!!","owner":"Andrew"},
                        ],
               "125": [{"recommentations":"Can I use onion powder instead of onion??","owner":"AndyGr"},
                         {"recommentations":"I didn’t have any eggs, so I replaced them with a banana-chia-flaxseed pulse. It turned out terrible; this recipe is terrible.","owner":"Andrew"},
                         {"recommentations":"Simple and delicious!! I served this with a mozarella smoked chicken ravioli. Thank for the recipe","owner":"AdamSmith"},
                        ],
               "129": [{"recommentations":"One of the best vegetarian dishes I ever tried!! thanks ","owner":"AndyGr"},
                        ],
               "130": [{"recommentations":"I made it with cod instead of salmon, still delicious","owner":"JohnBrown"},
                         {"recommentations":"Not as good as it seems. I was disappointed","owner":"Andrew"},
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
                         new_comment = add_comment(comment['recommentations'],comment_user,new_recipe)

     # display all the recipes with their category
     for category in Category.objects.all():
          for recipe in Recipe.objects.filter(category_id = category):
               print("-{}-{}".format(category.name,recipe.name))


     # add randomly recipes to the users as saved recipes
     recipes = Recipe.objects.all()
     for user in User.objects.all():
          num_of_saved_recipes = random.choice([2,3,4,5,6])
          userProf = UserProfile.objects.get(id = user.id)
          for i in range(num_of_saved_recipes):
               recipe = random.choice(recipes)
               userProf.saved_Recipes.add(recipe)


     




# helper function to save comments
def add_comment(recommentation,owner,recipe):
     category = Comment.objects.get_or_create(recommentations=recommentation,owner_id=owner,recipe_id=recipe)[0]
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

