from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

from datetime import datetime

from ready_recipe.models import *
from ready_recipe.forms import *
from django.contrib.auth.models import User
from django.urls import reverse

from django.template.defaultfilters import slugify






def index(request):
    category_list = Category.objects.order_by('-name')
    #recipe_list = Recipe.objects.order_by('-views')[:5]


    context_dict={}
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
        recipe = Recipe.objects.get(slug = recipe_name_slug)
        comment = Comment.objects.filter(recipe_id = recipe.id )
           
        context_dict['recipes'] = recipe
        context_dict['comments'] = comment

        if request.user.is_authenticated:
            # current_user refers to UserProfile 
            # request.user refers to User
            current_user, created = UserProfile.objects.get_or_create(user1 = request.user)
            context_dict['Owner'] = request.user
            if recipe in  current_user.saved_Recipes.all():
                button_text = 'Remove from Saved Recipes'
            else:
                button_text = 'Add to Saved Recipes'

            context_dict['button'] = button_text

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
                comment.owner_id = request.user
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
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                login(request, user)
                return redirect(reverse('ready_recipe:index'))
        else:
            context_dict["success"] = False
            return render(request, 'ready_recipe/login.html',context_dict)
    else:
        context_dict["success"] = True
        return render(request, 'ready_recipe/login.html',context_dict)



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
            recipe.owner_id = current_user
            recipe.save()
            recipe_slug = slugify(recipe.name)
            category_slug = slugify(recipe.category_id.name)
            return HttpResponseRedirect(reverse('ready_recipe:show_recipe',args=(category_slug,recipe_slug,)))

        else:
            print(form.errors)
    else:
        form = RecipeForm()
    return render(request,'ready_recipe/add_recipe.html',{'form':form})


@login_required
def add_category(request):
    form = CategoryForm()
    if request.user.is_superuser:
        if request.method =='POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=True)
                return HttpResponseRedirect(reverse('ready_recipe:index'))
            else:
                print(form.errors)
    else:
        return HttpResponseRedirect(reverse('ready_recipe:index'))

    return render(request,'ready_recipe/add_category.html',{'form':form})




def get_recipe_info(recipes_qs):
    recipes_info = []
    for recipe in recipes_qs.all():
        category_slug = slugify(recipe.category_id.name)
        recipe_slug = slugify(recipe.name)
        recipes_info.append([recipe,category_slug,recipe_slug])
    return recipes_info

@login_required
def user_profile(request):
    context_dict={}
    
    current_user, created = UserProfile.objects.get_or_create(user1 = request.user)

    # recipes added by the current user
    my_recipes = Recipe.objects.filter(owner_id = request.user.id)

    # recipes saved by the current user
    fav_recipes = current_user.saved_Recipes.all()
 
    context_dict['own_rec_info'] = get_recipe_info(my_recipes)
    context_dict['fav_rec_info'] = get_recipe_info(fav_recipes)


    return render(request,'ready_recipe/user_profile.html',context=context_dict)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'ready_recipe/change_password.html', {'form': form})    

@login_required
def delete_user(request,username):
    current_user = User.objects.get(username = username)
    current_user.delete()
    return redirect(reverse('ready_recipe:index'))


@login_required
def add_or_delete_recipe(request,primaryKey):

    recipe = Recipe.objects.get(id = primaryKey)
    current_user, created = UserProfile.objects.get_or_create(user1 = request.user)
    recCategory = Category.objects.get(id = recipe.category_id.id)    
    # if recipe exists in the saved recipes of the current user delete it
    # if not add it
    if recipe in current_user.saved_Recipes.all():
        #remove the recipe from saved_Recipes
        current_user.saved_Recipes.remove(recipe)
    else:
        # add the recipe to saved_Recipes
        current_user.saved_Recipes.add(recipe)

    cat = slugify(recCategory.name)
    rep = slugify(recipe.name)
    return HttpResponseRedirect(reverse('ready_recipe:show_recipe',args=(cat,rep,)))
    

def search_helper(sort_by,attri,rec_qs):
    results_info=[]
    messages = {1:'Price per portion: £',2:'Price per portion: £',3:'Difficulty: ',4:'Calories per portion: ',5:'Completion time: ',6:'Portion: '}
    for recipe in rec_qs:
        results_info.append([recipe,slugify(recipe.category_id.name),slugify(recipe.name),messages[sort_by],getattr(recipe,attri)])
    return results_info

        


def search(request,search=None,sorting=None):
    context_dict={}
    results=[]
    recipes = Recipe.objects.all()

    if request.method == 'POST':
        search = request.POST.get("search")
    if (not search.strip()) or search=="All the recipes" or (not search):
        results = recipes
        search="All the recipes"

    else:
        search_split = search.split()
        for recipe in recipes:
            for se in search_split:
                if se.lower() in recipe.name.lower():
                    results.append(recipe)

    results_info=[]
    if sorting=='1':
        results = sorted(results, key=lambda rec: rec.average_overall_price) 
        results_info = search_helper(1,'average_overall_price',results)
        context_dict['message'] = 'Price(low to high)'


    elif sorting=='2':
        results = sorted(results, key=lambda rec: rec.average_overall_price,reverse=True )
        results_info = search_helper(2,'average_overall_price',results)
        context_dict['message'] = 'Price(high to low)'

    elif sorting=='3':
        results = sorted(results, key=lambda rec: rec.difficulty )    
        results_info = search_helper(3,'difficulty',results)
        context_dict['message'] = 'Difficulty(low to high)'
 
    elif sorting=='4':  
        results = sorted(results, key=lambda rec: rec.calories)
        results_info = search_helper(4,'calories',results)    
        context_dict['message'] = 'Calories(low to high)'
   
    elif sorting=='5':
        results = sorted(results, key=lambda rec: rec.completion_time)     
        results_info = search_helper(5,'completion_time',results)     
        context_dict['message'] = 'Time Needed(low to high)'     
  
    elif sorting=='6':    
        results = sorted(results, key=lambda rec: rec.portions)   
        results_info = search_helper(6,'portions',results)     
        context_dict['message'] = 'Portions(low to high)'     
  
    else:
        for recipe in results:
            category_slug = slugify(recipe.category_id.name)
            recipe_slug = slugify(recipe.name)
            results_info.append([recipe,category_slug,recipe_slug,'',''])
            context_dict['message'] = 'Sort By'



    context_dict['results'] = results_info
    context_dict['search'] = search

    return render(request,'ready_recipe/search.html',context_dict)