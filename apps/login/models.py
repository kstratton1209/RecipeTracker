from django.db import models
import re
import bcrypt

class RegistrationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"       
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address. Please try again"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['password_confirm']:
            errors["passwordConfirm"] = "Passwords must match. Please try again."
        user = self.filter(email = postData["email"])
        if user:
             errors["email_exists"] = "Email already exists."
        return errors
    def login_validator(self, postData):
        user = Registration.objects.filter(email = postData['email'])
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['password']) == 0:
            errors["password"] = "Please enter a password."
        if len(postData['email']) == 0:
            errors["email"] = "Please enter an email."
        else:
            if user:
                logged_user = user[0]
                if bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                    print("password found")
                else:
                    errors["confirm"] = "Password or email is incorrect. Please try again."
            else:
                errors["email_not_found"]="No account associated with that email"
        return errors


class Registration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegistrationManager()


