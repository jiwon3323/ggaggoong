from django.http.response import JsonResponse
from django.shortcuts import render
import time, random, sys, traceback, logging, datetime, json
from faq.models import FAQ, FAQ_Answer
from user.models                import User, Host
from content.models                import Contents,Contents_Detail

# Create your views here.

def faq_question(request):
    jsonObject = json.loads(request.body)
    tmp_user_name = User.objects.get(id = jsonObject.get('questioner')).email
    tmp_created_at = str(datetime.datetime.now())
    faq = FAQ()

    faq.questioner = User.objects.get(id = jsonObject.get('questioner'))
    faq.faq_content = Contents.objects.get(id = int(jsonObject.get('faq_content')))
    faq.question = jsonObject.get('question')
    

    faq.save()

    context={
        'question' : faq.question,
        'questioner' : tmp_user_name,
        # 'faq_content' : faq.faq_content,
        'created_at' : tmp_created_at,
        'updated_at' : faq.updated_at,
    }
    return JsonResponse(context)



def faq_answer(request):
    jsonObject = json.loads(request.body)
    tmp_user_name = User.objects.get(id = jsonObject.get('answerer')).email
    tmp_created_at = str(datetime.datetime.now())
    faq_answer = FAQ_Answer()

    faq_answer.answerer = Host.objects.get(user_id = jsonObject.get('answerer'))
    faq_answer.question_id = FAQ.objects.get(id = int(jsonObject.get('question_id')))
    faq_answer.answer = jsonObject.get('answer')
    

    faq_answer.save()

    context={
        'answer' : faq_answer.answer,
        'answerer' : tmp_user_name,
        # 'faq_content' : faq.faq_content,
        'created_at' : tmp_created_at,
        'updated_at' : faq_answer.updated_at,
    }
    return JsonResponse(context)