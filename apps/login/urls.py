from django.urls import path     
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('success',views.success),
    path('logout',views.logout),
    path('registerVal',views.ajaxregister),
    path('bio',views.bio),
    path('addBio',views.addBio),

]