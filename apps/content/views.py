from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import Recipes, Registration
import requests



def home(request):
    if 'id' in request.session:
        context = {
            'all_the_recipes': Recipes.objects.all(),
            # 'recipes_user_made':
            # 'user_wants_to_make':
            'recipes_mains': Recipes.objects.filter(category = 'Main'),
            'recipes_desserts': Recipes.objects.filter(category = 'Dessert'),
            'recipes_sides': Recipes.objects.filter(category = 'Side'),
            'recipes_appetizers': Recipes.objects.filter(category = 'Appetizer'),
            "logged_user": Registration.objects.get(id = request.session['id']),
        }
        return render(request,"home.html",context)
    else:
        return redirect("/")

def addRecipe(request):
    context = {
            'all_the_recipes': Recipes.objects.all()
        }
    return render(request,"addRecipe.html", context)

def createRecipe(request):
    errors = Recipes.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/content/addRecipe")
    else:
        title_from_form = request.POST['recipe_title']
        source_from_form = request.POST['source']
        category_from_form = request.POST['category']
        user_id = int(request.POST['user_id'])
        url_from_form = request.POST['url']
        img_from_form = request.POST['img']
        status_from_form = request.POST['status']
            
        logged_user = Registration.objects.get(id = user_id)

        
     
        Recipes.objects.create(title = title_from_form, user = logged_user, source = source_from_form, category = category_from_form, url= url_from_form, img = img_from_form)

        if status_from_form == "Made it!":
            this_recipe = Recipes.objects.filter(url = url_from_form)
            if this_recipe:
                recipe = this_recipe[0]
                recipe.already_made.add(logged_user)
        else:
            this_recipe = Recipes.objects.filter(url = url_from_form)
            if this_recipe:
                recipe = this_recipe[0]
                recipe.want_to_make.add(logged_user)

        return redirect('/content/home')

def recipeDetails(request,id):
    id = int(id)
    this_recipe = Recipes.objects.get(id = id)
    context = {
        'recipe': this_recipe
    }
    return render(request,"recipeDetails.html", context)

def likeRecipe(request,id,user_id):
    id = int(id)
    user_id = int(user_id)
    status = request.POST['status']
    print(status)
    logged_user = Registration.objects.get(id = user_id)
    this_recipe = Recipes.objects.get(id = id)


    if status == 'Want to try it!':
        print("user clicked wants to try it")
        this_recipe.want_to_make.add(logged_user)
    elif status == 'Made it!':
        print("user clicked already made")
        this_recipe.already_made.add(logged_user)
    return redirect('/content/home')    

def myRecipes(request,user_id):
    user_id = int(user_id)
    context = {
        'logged_user_recipes': Recipes.objects.filter(user=user_id),
        'recipes_interested': Recipes.objects.filter(want_to_make=user_id),
        'recipes_made': Recipes.objects.filter(already_made=user_id),
        'logged_user': Registration.objects.get(id = user_id)
    }
    return render(request,"myRecipes.html", context)

def searchRecipe(request):
    
    return render(request,"searchRecipe.html")

def discoverRecipe(request):
    # https://developer.edamam.com/edamam-docs-recipe-api
    # APP_ID = 'e80aeb5e'
    # API_KEY = '6d2433ca65fc15720626718ed3460c04'
    search_from_form = request.POST['search_item']
    searchresults = requests.get("https://api.edamam.com/search?app_id=e80aeb5e&app_key=6d2433ca65fc15720626718ed3460c04&q="+search_from_form)

    searchresults = searchresults.json()
    context = {
        'reciperesults': searchresults['hits'],
    }
    
    
    return render(request,'searchRecipe.html',context)


def addRecipeSearch(request,recipeLabel,recipeSource):
    recipeNameToAdd = recipeLabel
    recipeSourceToAdd = recipeSource
 
     
    context = {
            'all_the_recipes': Recipes.objects.all(),
            'recipeName': recipeNameToAdd,
            'recipeSource': recipeSourceToAdd,
        }
    return render(request,"addRecipe.html", context)

def category(request,category):
    category_from_menu = category
    context = {
            'recipe_by_category': Recipes.objects.filter(category = category_from_menu)
        }
    return render(request,"category.html", context)
