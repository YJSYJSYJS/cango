from django.shortcuts import render

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
        return render(request, 'register.html', res_data)