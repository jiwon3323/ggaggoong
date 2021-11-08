from django.shortcuts           import render
from django.contrib             import auth
# from ggaggoong.user.models      import Host
from user.models                import User, Host
from django.shortcuts           import render, redirect
from django.shortcuts           import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime                   import datetime
from django.utils               import formats
from django.utils.dateformat    import DateFormat
from django.utils.formats       import get_format
import json, re
from django.http                import JsonResponse
from django.views               import View
from django.core.exceptions     import ValidationError
# from .utils                     import validate_email, validate_password


def home(request):
    return render(request, 'home.html')
# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2'] and len(request.POST['password1']) >= 5:
            try:
                
                if not validate_email(request.POST['email']):
                    return JsonResponse({'MESSAGE':'INVALID_EMAIL_ADDRESS'}, status=404)

                if not validate_password(request.POST['password1']):
                    return JsonResponse({'MESSAGE':'INVALID_PASSWORD'}, status=404)

            except KeyError:
                return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=404)
            except ValidationError as e:
                return JsonResponse({'MESSAGE':e.message}, status=404)
            user = User.objects.create_user(
                    username=request.POST['mom_name'],
                    email=request.POST['email'],
                    mom_name=request.POST['mom_name'],
                    password=request.POST['password1'],
                    baby_name=request.POST['baby_name'],
                    baby_gender=request.POST['baby_gender'],
                    baby_birth=request.POST.get('baby_birth'),
                    phone=request.POST['phone_num'],
                    address=request.POST['address'],
                    
                    )
            if user is not None:
                auth.login(request, user)
                return redirect('/user/home') #render(request, 'home.html', {'user':user})
    print("회원가입 안됨")
    return render(request, 'signup.html') 

def host_signup(request):
    print(request.user.id)
    if request.method == 'POST':
        if request.user.id:
            print(request.user.id)
            # user = User()
            host = Host()
            host.user_id = get_object_or_404(User, id=request.user.id)
            host.id_card = request.POST["id_card"]
            host.certificate_id = request.POST["certificate_id"]
            try: # request.FILES["crimelog"]:
                host.crimelog = request.FILES["crimelog"]
            except:
                pass
            host.crime_bool = request.POST["crime_bool"]
            try: # request.FILES["bank_img"]:
                host.bank_img = request.FILES["bank_img"]
            except:
                pass
            host.bank_num = request.POST["bank_num"]
            host.save()
            if host is not None:
                # auth.login(request, user)
                return redirect('/user/home')
    print("회원가입 안됨")
    return render(request, 'host_signup.html')

def login(request):
    if request.method == 'GET':
        error_message = '로그인페이지입니다.'
        return render(request, 'login.html', {'error_message':error_message})
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)        
        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html', {'user':user})
    error_message = '잘못된 요청입니다. 다시 로그인해주세요.'  
    return render(request, 'login.html', {'error_message':error_message})


def validate_email(email):
        return re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) != None 

def validate_password(password):
        return len(password)>=5

def duplicate_email_check(email):
        return User.objects.filter(email=email).exists() 
