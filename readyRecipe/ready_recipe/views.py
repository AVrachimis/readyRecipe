from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse



from ready_recipe.models import *
from ready_recipe.forms import *
from django.contrib.auth.models import User
from django.urls import reverse

from django.template.defaultfilters import slugify
from datetime import datetime

def get_server_side_cookie(request, cookie, default_val=0):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], "%Y-%m-%d %H:%M:%S")

    if (datetime.now() - last_visit_time).seconds > 0:
        visits += 1
        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits


def index(request):
    category_list = Category.objects.order_by('-name')

    context_dict={}
    context_dict['categories'] = category_list

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'ready_recipe/index.html', context=context_dict)
    return response



def show_category(request, category_name_slug):
    context_dict={}

    try: 
        # find a category with the given slug
        category = Category.objects.get(slug = category_name_slug)
        
        # queryset with the recipes of the given category
        recipes = Recipe.objects.filter(category_id=category)
        
        # add recipes and categories to the context_dict
        context_dict['recipes'] = recipes
        context_dict['category'] = category
    
    # if category does not exist
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['recipes'] = None

    return render(request, 'ready_recipe/category.html', context=context_dict)



def show_recipe(request, category_name_slug, recipe_name_slug):
    context_dict={}

    try: 
        # get the recipe with the given slug
        recipe = Recipe.objects.get(slug = recipe_name_slug)
        # get all the comments of the current recipe
        comment = Comment.objects.filter(recipe_id = recipe.id )
        
        # add recipe and comments to the contect_dict
        context_dict['recipes'] = recipe
        context_dict['comments'] = comment

        # check whether the user is logged in
        if request.user.is_authenticated:

            # current_user refers to UserProfile 
            # request.user refers to User
            current_user, created = UserProfile.objects.get_or_create(user1 = request.user)
            
            # check if the current recipe exists in the saved recipes of the user
            # and adjust the button text accordingly
            if recipe in  current_user.saved_Recipes.all():
                button_text = 'Remove from Saved Recipes'
            else:
                button_text = 'Add to Saved Recipes'

            context_dict['button'] = button_text

            # also, add the comment form
            form = CommentForm()
            context_dict['form'] = form
        else:

            context_dict['form'] = None

        # comment form
        if request.method =='POST':
            form = CommentForm(request.POST)

            # recipe id is the id of the current recipe
            # and owner id is the id of the logged in user
            if form.is_valid():
                comment = form.save(commit = False)
                comment.recipe_id = recipe
                comment.owner_id = request.user
                comment.save()
                return HttpResponseRedirect(reverse('ready_recipe:show_recipe',args=(category_name_slug,recipe_name_slug,)))

            else:
                print(form.errors)

    except Recipe.DoesNotExist:
        context_dict['recipes'] = None
        context_dict['comments'] = None
        context_dict['form'] = None

    return render(request, 'ready_recipe/recipe.html', context=context_dict)



def register(request):
    context_dict = {}

    if request.method == 'POST':
        # user and userprofile forms
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        # check if both are valid and connect user with userprofile
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user1 = user
            profile.save()
            new_user = authenticate(username=user_form.cleaned_data['username'],password = user_form.cleaned_data['password'])
            # once the account is created, log in and redirect to the index page
            login(request,new_user)
            return HttpResponseRedirect(reverse('ready_recipe:index'))

    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict["user_form"] = user_form
    context_dict["profile_form"] = profile_form
    return render(request, 'ready_recipe/register.html', context_dict)



def user_login(request):
    context_dict = {}
    # if user is already logged in redirect it to the index page
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        # get the username and password and try to log in
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        # if the information given are corrent, log in and redirect to index page
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('ready_recipe:index'))
        else:
            # else error messages appear and user can try again
            context_dict["success"] = False
            return render(request, 'ready_recipe/login.html',context_dict)
    else:
        context_dict["success"] = True
        return render(request, 'ready_recipe/login.html',context_dict)



@login_required
def user_logout(request):
    #Since we knoare sure that the user is logged 
    # in because of the @login_required, we can just log out
    logout(request)
    #take the user back to the homepage
    return redirect(reverse('ready_recipe:index'))


@login_required
def add_recipe(request):
    context_dict={}
    try:
        # get the current user
        current_user = User.objects.get(id = request.user.id)
        if request.method == 'POST':
            # form to upload your own recipe
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                # owner of the recipe is the current user
                # save the recently created recipe and redirect to the page of that recipe
                recipe = form.save(commit = False)
                recipe.owner_id = current_user
                recipe.save()
                return HttpResponseRedirect(reverse('ready_recipe:show_recipe',args=(slugify(recipe.category_id.name),slugify(recipe.name),)))
            else:
                print(form.errors)
        else:
            form = RecipeForm()

        context_dict['form'] = form

    except Recipe.DoesNotExist:
        context_dict['form'] = None

    return render(request,'ready_recipe/add_recipe.html',context=context_dict)


# it can be used only from the admins to add new categories
@login_required
def add_category(request):
    form = CategoryForm()
    # check whether the logged in user is admin
    # and if yes, it add the new category without any recipes in it
    if request.user.is_superuser:
        if request.method =='POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=True)
                return HttpResponseRedirect(reverse('ready_recipe:index'))
            else:
                print(form.errors)
    else:
        # if user not an admin, redirect it to the home page
        return HttpResponseRedirect(reverse('ready_recipe:index'))

    return render(request,'ready_recipe/add_category.html',{'form':form})



# helper function which returns a list of list
# inner list has the object of the recipe, the category slug of the recipe and the recipe slug
def get_recipe_info(recipes_qs):
    recipes_info = []
    for recipe in recipes_qs.all():
        category_slug = slugify(recipe.category_id.name)
        recipe_slug = slugify(recipe.name)
        recipes_info.append([recipe,category_slug,recipe_slug])
    return recipes_info

# profile of the user
# it inludes the recipes uploaded by the current user and the saved recipes
@login_required
def user_profile(request):
    context_dict={}
    
    # get the userProfile of the current user
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
    # get the current user and delete is from the database and then redirect to the index page
    current_user = User.objects.get(username = username)
    current_user.delete()
    return redirect(reverse('ready_recipe:index'))

# function to add or remove a recipe from the saved recipes of the current user
@login_required
def add_or_delete_recipe(request,primaryKey):

    # get the recipe the userProfile of the currentUser and the category of the current recipe
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

    return HttpResponseRedirect(reverse('ready_recipe:show_recipe',args=(slugify(recCategory.name),slugify(recipe.name),)))
    


# helper function used when sorting the search results
# it returns a list of lists
# inner list structure: [the-recipe-object, slug-of-the-category, slug-of-the-recipe, message-under-the-recipe, value-of-the-attribute-sorted ]
def search_helper(sort_by,attri,rec_qs):
    results_info=[]
    messages = {1:'Price per portion: £',2:'Price per portion: £',3:'Difficulty: ',4:'Calories per portion: ',5:'Completion time: ',6:'Portion: '}
    for recipe in rec_qs:
        results_info.append([recipe,slugify(recipe.category_id.name),slugify(recipe.name),messages[sort_by],getattr(recipe,attri)])
    return results_info


# this function is called in two cases:
#                       1-when searching: no other paremeters except request
#                       2-when sorting: both optional parameters are used
def search(request,search=None,sorting=None):
    context_dict={}
    results=[]
    # get all the recipes in tha database
    recipes = Recipe.objects.all()
    context_dict['all_recipes'] = recipes


    # method is post only when searching, not when sorting
    if request.method == 'POST':
        search = request.POST.get("search")
    
    # check for blank or empty string. if true, all the recipes of the database are listed
    if (not search.strip()) or search=="All the recipes" or (not search):
        results = recipes
        search="All the recipes"

    else:
        # otherwise split the user input and make search with all the words of the input
        search_split = search.split()
        for recipe in recipes:
            for se in search_split:
                if se.lower() in recipe.name.lower():
                    results.append(recipe)

    results_info=[]

    # if statemets are executed when sorting
    # each if is different sorting
    # the else statement at the end, is the default where not sorting is executed
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


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                                'last_visit',
                                                str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits