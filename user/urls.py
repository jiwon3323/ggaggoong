from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('host_signup/', views.host_signup, name="host_signup"),
    # path('login_success/', views.login_success, name="login_success"),
]
