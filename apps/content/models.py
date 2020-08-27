from django.db import models
from django.conf import settings
from apps.login.models import Registration, Profile
import re

# From settings.py
ALLOWED_EXTENSIONS = settings.ALLOWED_EXTENSIONS
MAX_UPLOAD_SIZE = settings.MAX_UPLOAD_SIZE


# Create your models here.
class RecipesManager(models.Manager):
    def basic_validator(self, postData, fileData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['recipe_title']) < 4:
            errors["title"] = "A recipe must consist of at least 3 characters."
        if len(postData['source']) < 1:
            errors["source"] = "A source must be provided!"
        recipe = self.filter(url = postData["url"])
        if recipe:
            errors["recipe_exists"] = "Recipe has already been added."  
        if fileData["img"].name.find(".") == -1:
            errors["type"]="Image must be '.jpg', '.jpeg', '.gif', or '.png'"
        elif fileData["img"].name.split(".")[-1].lower() not in ALLOWED_EXTENSIONS:
            errors["type"]="Image must be '.jpg', '.jpeg', '.gif', or '.png'"
        elif fileData["img"].size > MAX_UPLOAD_SIZE:
            errors["image"]="Image must 5MB or less in size"       
        return errors
    def edit_validator(self, postData, fileData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['recipe_title']) < 4:
            errors["title"] = "A recipe must consist of at least 3 characters."
        if len(postData['source']) < 1:
            errors["source"] = "A source must be provided!"
        if "img" not in fileData:
            errors["image"]="Must upload an image."
        elif fileData["img"].name.find(".") == -1:
            errors["type"]="Image must be '.jpg', '.jpeg', '.gif', or '.png'"
        elif fileData["img"].name.split(".")[-1].lower() not in ALLOWED_EXTENSIONS:
            errors["type"]="Image must be '.jpg', '.jpeg', '.gif', or '.png'"
        elif fileData["img"].size > MAX_UPLOAD_SIZE:
            errors["image"]="Image must 5MB or less in size"       
        return errors
        
class Recipes(models.Model):
    user = models.ForeignKey(Registration, related_name = "user_recipes", on_delete = models.CASCADE)
    title = models.TextField()
    source = models.TextField()
    category = models.TextField()
    url = models.TextField()
    img = models.ImageField(upload_to="forums", default=None, blank=True, null=True)
    notes = models.TextField()
    want_to_make = models.ManyToManyField(Registration, related_name = "user_wants_to_make")
    already_made = models.ManyToManyField(Registration, related_name = "user_already_made")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RecipesManager()

class Reviews(models.Model):
    user = models.ForeignKey(Registration, related_name = "user_reviews", on_delete = models.CASCADE)
    stars = models.IntegerField()
    headline = models.TextField()
    review = models.TextField()
    recipe = models.ManyToManyField(Recipes, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    user = models.ManyToManyField(Registration, related_name = "user_comments")
    review = models.ManyToManyField(Reviews, related_name="review_comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)