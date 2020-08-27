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
    path('<id>/review',views.addReview),
    path('<id>/createReview',views.createReview),
    path('<id>/<review_id>/deleteReview',views.deleteReview),
    path('<user_id>/<id>/delete', views.deleteRecipe),
    path('<user_id>/<id>/edit', views.editRecipe),
    path('<user_id>/<id>/update', views.updateRecipe),
    path('<user_id>/<follow_id>/follow', views.addFollow),
    path('<user_id>/<follow_id>/unfollow', views.unfollow),



    # path('granted', views.granted)
]