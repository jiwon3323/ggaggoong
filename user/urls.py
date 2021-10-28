from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path('singup/', views.signup, name="sign_up"),
    path('home/', views.home, name="home"),
]
