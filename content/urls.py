from django.urls import path

from content import views
app_name = 'Content'
urlpatterns = [
    path("make/", views.con_making, name="content_make"),
    path("page/<int:content_number>/", views.con_page, name='content_detail'),
    path("reserve<int:content_number>/", views.reserve, name='reserve'),
    path("pay_page", views.pay_page, name='pay_page'),
]