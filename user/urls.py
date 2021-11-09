from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('user_update/', views.user_update, name="user_update"),
    path('host_signup/', views.host_signup, name="host_signup"),
    # path('host_login/', views.host_login, name="host_login"),
    path('host_update/', views.host_update, name="host_update"),
    # path('login_success/', views.login_success, name="login_success"),
]
