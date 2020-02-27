from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime


from ready_recipe.models import Recipe


def index(request):
    
    recipe_list = Recipe.objects.order_by('-views')[:5]
    context_dict={}
    context_dict['boldmessage'] = 'Hello i have just started working with the project!!'
    context_dict['recipes'] = recipe_list
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
        pages = Page.objects.filter(category=category)
        
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the response and return it to the client.
    return render(request, 'ready_recipe/category.html', context=context_dict)
    



@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return redirect('/rango/')
        else:
            print(form.errors)

    return render(request,'ready_recipe/add_category.html',{'form':form})




    
@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

        
    if category is None:
        return redirect('/rango/')
    
    form = PageForm()
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'ready_recipe/add_page.html', context=context_dict)
