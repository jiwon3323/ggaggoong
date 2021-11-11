from django.urls import path

from faq import views

urlpatterns = [
    path("faq_question/", views.faq_question, name='faq_question'),
    path("faq_answer/", views.faq_answer, name='faq_answer'),
]