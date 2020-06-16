from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Puser
from .forms import LoginForm
from planner.views import day

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('planner:day')
            # return render(request, 'planner/day.html', {'form': form})
    else:
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
            return render(request, 'register/register.html', res_data)
        
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'register/register.html', res_data)
        else:
            puser = Puser(
                username=username,
                useremail = useremail,
                password=make_password(password)
            )
            puser.save()


        return redirect('/')
        