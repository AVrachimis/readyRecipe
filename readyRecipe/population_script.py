import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','readyRecipe.settings')


import django
django.setup()
from rango.models import *


def populate():

    users = {"user1":{"username":"AdamSmith","email":"ASmith@hotmail.com"   },
             "user2":{"username":"JohnBrown","email":"JohnB@hotmail.com"   },
             "user3":{"username":"GeorgeJr","email":"GeorgeJR@hotmail.com"   },
             "user4":{"username":"AndyGr","email":"AGround@hotmail.com"   },
             "user5":{"username":"Andrew","email":"A_Jack@hotmail.com"   },

            }

     # create users
     for user,user_info in users.items():
          user = User.objects.get_or_create(username=user_info['username'],email=user_info['email'])
          
          userProfile = UserProfile.objects.get_or_create(user = user,)


    # categories with recipes
    chicken = [{"id": "ch1",
                     "name": "Chicken Tikka Masala",
                     "ingredients": " ",
                     "instructions": " ",
                     "price": 2.10,
                     "category": "chicken",
                     "user": "AdamSmith",
                     "picture": "",
                     "portions": 3,
                     "difficulty": 2,
                     "completion_time": "15-30 minutes",
                     "calories": "489",
                },


                {"id": "ch2",
                     "name": "Introduction to Calculus",
                     "ingredients": " ",
                     "instructions": " ",
                     "price": 70,
                     "category": "chicken",
                     "user": "ChristopherSmith",
                     "picture": "",
                     "portions": "",
                     "difficulty": "",
                     "completion_time": "",
                     "calories": "",
                }]


    desserts=[{"id": "ch2",
                     "name": "Introduction to Calculus",
                     "ingredients": " ",
                     "instructions": " ",
                     "price": 70,
                     "category": "chicken",
                     "user": "ChristopherSmith",
                     "picture": "",
                     "portions": "",
                     "difficulty": "",
                     "completion_time": "",
                     "calories": "",
                },
                
                {"id": "ch2",
                     "name": "Introduction to Calculus",
                     "ingredients": " ",
                     "instructions": " ",
                     "price": 70,
                     "category": "chicken",
                     "user": "ChristopherSmith",
                     "picture": "",
                     "portions": "",
                     "difficulty": "",
                     "completion_time": "",
                     "calories": "",
                }]


    categories = {"chicken":}


        comments = {"sch1": [{"comment": "I am interested!", "user": "Maria"},
                         {"comment": "Hey Maria, you can send me an email so we can discuss the details", "user": "JohnPope"}],
                "sch2": [{"comment": "Just send you an email", "user": "Veronica"},
                         {"comment": "I really need this book, I can make a you a better offer.", "user": "PeterBrown"}],
                "sch3": [{"comment": "Comment by user Batman here", "user": "Batman"},
                         {"comment": "Reply by user James", "user": "James"}],
                "ele1": [{"comment": "I am interested!", "user": "ChristopherSmith"},
                         {"comment": "Hey Christopher, you can send me an email so we can discuss the details", "user": "James"}],
                "ele2": [{"comment": "Just send you an email", "user": "PeterBrown"},
                         {"comment": "I really need this phone, I can make a you a better offer. Check your email.", "user": "JohnPope"}],
                "ele3": [{"comment": "Comment by user here", "user": "Batman"},
                         {"comment": "Reply by user", "user": "James"}],
                "clo1": [{"comment": "Comment on clothing item 1", "user": "JohnPope"},
                         {"comment": "Another comment on clothing item 1", "user": "ChristopherSmith"}],
                "clo2": [{"comment": "Comment on clothing item 2", "user": "PeterBrown"},
                         {"comment": "Another comment on clothing item 2", "user": "James"}],
                "clo3": [{"comment": "Comment on clothing item 3", "user": "Veronica"},
                         {"comment": "Another comment on clothing item 3", "user": "Maria"}],
                "hom1": [{"comment": "Comment on homeware item 1", "user": "Victor"},
                         {"comment": "Another comment on homeware item 1", "user": "Batman"}],
                "hom2": [{"comment": "Comment on homeware item 2", "user": "JohnPope"},
                         {"comment": "Another comment on homeware item 2", "user": "ChristopherSmith"}],
                "hom3": [{"comment": "Comment on homeware item 3", "user": "PeterBrown"},
                         {"comment": "Another comment on homeware item 3", "user": "James"}],
                "spo1": [{"comment": "Comment on sports item 1", "user": "Veronica"},
                         {"comment": "Another comment on sports item 1", "user": "Maria"}],
                "spo2": [{"comment": "Comment on sports item 2", "user": "Victor"},
                         {"comment": "Another comment on sports item 2", "user": "Batman"}],
                "spo3": [{"comment": "Comment on sports item 3", "user": "JohnPope"},
                         {"comment": "Another comment on sports item 3", "user": "ChristopherSmith"}],
                "oth1": [{"comment": "Comment on others item 1", "user": "PeterBrown"},
                         {"comment": "Another comment on others item 1", "user": "James"}],
                "oth2": [{"comment": "Comment on others item 2", "user": "Veronica"},
                         {"comment": "Another comment on others item 2", "user": "Maria"}],
                "oth3": [{"comment": "Comment on others item 3", "user": "Victor"},
                         {"comment": "Another comment on others item 3", "user": "Batman"}]
                }




