from django.urls import path     
from . import views

urlpatterns = [
    path('home', views.home),
    path('addRecipe', views.addRecipe),
    path('addRecipe/<recipeLabel>/<recipeSource>', views.addRecipeSearch),
    path('createRecipe',views.createRecipe),
    path('recipe/<id>/details',views.recipeDetails),
    path('<id>/<user_id>/like',views.likeRecipe),
    path('<user_id>/myRecipes', views.myRecipes),
    path('searchRecipe',views.searchRecipe),
    path('discover',views.discoverRecipe),
    path('category/<category>',views.category),
    # path('granted', views.granted)
]