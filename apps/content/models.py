from django.db import models
from apps.login.models import Registration
import re

# Create your models here.
class RecipesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['recipe_title']) < 4:
            errors["title"] = "A recipe must consist of at least 3 characters."
        if len(postData['source']) < 1:
            errors["source"] = "A source must be provided!"
        recipe = self.filter(url = postData["url"])
        if recipe:
             errors["recipe_exists"] = "Recipe has already been added."     
        return errors

class Recipes(models.Model):
    user = models.ForeignKey(Registration, related_name = "user_recipes", on_delete = models.CASCADE)
    title = models.TextField()
    source = models.TextField()
    category = models.TextField()
    url = models.TextField()
    img = models.TextField()
    want_to_make = models.ManyToManyField(Registration, related_name = "user_wants_to_make")
    already_made = models.ManyToManyField(Registration, related_name = "user_already_made")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RecipesManager()