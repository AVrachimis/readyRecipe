from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

from ready_recipe.models import Recipe,Category,Comment,UserProfile
from ready_recipe.forms import RecipeForm,CommentForm,UserForm,UserProfileForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect





def index(request):
    category_list = Category.objects.order_by('-name')
    recipe_list = Recipe.objects.order_by('-views')[:5]


    context_dict={}
    context_dict['recipes'] = recipe_list
    context_dict['categories'] = category_list

    return render(request,'ready_recipe/index.html',context = context_dict)


def show_category(request, category_name_slug):
    #Create a context dictionary which we can pass to the template rendering engine
    context_dict={}

    try: 
        # we can find a category name slug with the given name?
        #if we can't, the .get() method raises a DoesNotExist exception
        category = Category.objects.get(slug = category_name_slug)
        
        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        recipes = Recipe.objects.filter(category_id=category)
        
        # Adds our results list to the template context under name pages.
        context_dict['recipes'] = recipes
        
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['recipes'] = None

    # Go render the response and return it to the client.
    return render(request, 'ready_recipe/category.html', context=context_dict)



def show_recipe(request, category_name_slug, recipe_name_slug):
    #Create a context dictionary which we can pass to the template rendering engine
    context_dict={}

    try: 
        # we can find a category name slug with the given name?
        #if we can't, the .get() method raises a DoesNotExist exception
        recipe = Recipe.objects.get(slug = recipe_name_slug)


        comment = Comment.objects.filter(recipe_id = recipe.id )
           
        context_dict['recipes'] = recipe
        context_dict['comments'] = comment

        #current_user = User.objects.get(id = request.user.id)
        if request.user.is_authenticated:
            current_user = request.user

            UserProfile.add_favourite_recipe(current_user,recipe)



            context_dict['Owner'] = current_user
            form = CommentForm()
            context_dict['form'] = form
        else:
            context_dict['Owner'] = None
            context_dict['form'] = None

        if request.method =='POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit = False)
                comment.recipe_id = recipe
                comment.owner_id = current_user
                comment.save()
                redirect_url = '/ready_recipe/category/'+category_name_slug+'/'+recipe_name_slug+'/'
                return redirect(redirect_url)
            else:
                print(form.errors)

    except Recipe.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        #context_dict['category'] = None
        context_dict['recipes'] = None
        context_dict['comments'] = None
        context_dict['form'] = None

    # Go render the response and return it to the client.
    return render(request, 'ready_recipe/recipe.html', context=context_dict)



def register(request):
    registered = False
    context_dict = {}
    if request.method == 'POST':
        #user_form = UserForm(request.POST)
        #profile_form = UserProfileForm()
        #context_dict['user_form'] = user_form
        #context_dict['profile_form'] = profile_form
        #context_dict["registered"] = registered
        #return render(request, 'ready_recipe/register.html', context=context_dict)

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password = user_form.cleaned_data['password'])
            login(request,new_user)


    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context_dict["user_form"] = user_form
    context_dict["profile_form"] = profile_form
    context_dict["registered"] = registered
    return render(request, 'ready_recipe/register.html', context_dict)



def user_login(request):
    context_dict = {}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:

                login(request, user)
                return redirect(reverse('ready_recipe:index'))
            else:
                return HttpResponse("Your account is disabled.")
                
        else:
            context_dict['success'] = False
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
            #return render(request, 'ready_recipe/login.html', context_dict)

    else:
        context_dict['success'] = True
        return render(request, 'ready_recipe/login.html', context_dict)



@login_required
def user_logout(request):
    #Since we know the user is logged in, we can now just log out
    logout(request)
    #take the user back to the homepage
    return redirect(reverse('ready_recipe:index'))


@login_required
def add_recipe(request):
    current_user = User.objects.get(id = request.user.id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit = False)
            recipe.views = 0
            recipe.owner_id = current_user
            recipe.save()
            return redirect('/ready_recipe/index/')
        else:
            print(form.errors)
    else:
        form = RecipeForm()
    return render(request,'ready_recipe/add_recipe.html',{'form':form})



@login_required
def user_profile(request):
    context_dict={}
    
    
    if request.user.is_authenticated:

        current_user, created = UserProfile.objects.get_or_create(user = request.user)

        my_recipes = Recipe.objects.filter(owner_id = request.user.id)

        # recipes saved by the current user
        fav_recipes = current_user.saved_Recipes.all()

    #for recipe in saved_recipes.all():
        #categoryId = str(recipe.category_id)
        #recipa = Recipe.objects.get(id = recipe.id).category_id
        #category = Category.objects.get(id = recipa)
       # category = str(Category.objects.get(id = categoryId))
        #recipe_category.append(category_id)
     #   recipe_category[recipe.name]=recipe.category_id

        context_dict['user'] = current_user
        context_dict['my_recipes'] = my_recipes
        context_dict['saved_recipes'] = fav_recipes


    return render(request,'ready_recipe/user_profile.html',context=context_dict)


  # recipe = Recipe.objects.get(slug = recipe_name_slug)


     #   comment = Comment.objects.filter(recipe_id = recipe.id )





