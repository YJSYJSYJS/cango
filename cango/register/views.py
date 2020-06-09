from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Puser
from .forms import LoginForm

def login(request):
    # if request.method == 'GET':
    #     return render(request, 'register/login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)

    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력해야합니다.'
    #     else:
    #         puser = Puser.objects.get(username=username)
    #         if check_password(password, puser.password):
    #             # 비밀번호가 일치 - 로그인 처리
    #             # 세션!
    #             # redirect
    #             request.session['user'] = puser.id # 세션마다 user키에 puser.id value를 넣어준다. 세션관리는 장고가 알아서 해줌
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '비밀번호가 틀렸습니다.'
        form = LoginForm()      
        return render(request, 'register/login.html', {'form': form})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')

def register(request):
    if request.method == 'GET':
        return render(request, 'register/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'

        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            puser = Puser(
                username=username,
                useremail = useremail,
                password=make_password(password)
            )
            puser.save()


        return render(request, 'register/register.html', res_data)