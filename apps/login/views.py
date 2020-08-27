# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .models import Registration, RegistrationManager, Profile
from django.contrib import messages
import bcrypt

def index(request):

    return render(request,"index.html")

def register(request):
    
    errors = Registration.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        first_name_from_form = request.POST['first_name']
        last_name_from_form = request.POST['last_name']
        email_from_form = request.POST['email']
        password_from_form = request.POST['password']

        pw_hash = bcrypt.hashpw(password_from_form.encode(), bcrypt.gensalt()).decode()
        Registration.objects.create(first_name=first_name_from_form, last_name= last_name_from_form, email = email_from_form, password=pw_hash)

        request.session['email']=email_from_form
        user = Registration.objects.filter(email = email_from_form)
        if user:
            logged_user = user[0]
            request.session['first_name']=logged_user.first_name
            request.session['email']=logged_user.email
            request.session['id']=logged_user.id

        return redirect('/bio')

def bio(request):
    return render(request,"bio.html")

def addBio(request):
    city_from_form = request.POST['city']
    state_from_form = request.POST['state']
    bio_from_form = request.POST['bio']
    age_from_form = int(request.POST['age'])
    user_id = int(request.POST['user_id'])
    profpic_from_form = request.FILES['profpic']

    logged_user = Registration.objects.get(id = user_id)

    Profile.objects.create(city = city_from_form, user = logged_user, state = state_from_form, age = age_from_form, profpic = profpic_from_form, bio = bio_from_form)


    return redirect('/success')




def login(request):
    
    errors = Registration.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = Registration.objects.filter(email = request.POST['email'])
        logged_user = user[0]
        request.session['first_name']=logged_user.first_name
        request.session['id']=logged_user.id
        return redirect('/success')
    
def ajaxregister(request):
    filterresult = Registration.objects.filter(email = request.POST['email'])
    
    if len(filterresult)>0:
        emailfound = True
    else:
        emailfound = False
    
    context = {
            'emailfound':emailfound
        }

    return render(request,'response.html', context)

def success(request):
    return redirect("content/home")

def logout(request):
    request.session.clear()
    return redirect("/")

