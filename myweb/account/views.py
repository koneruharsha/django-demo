from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        if request.POST['upass'] == request.POST['cupass']:
            if User.objects.filter(email=request.POST['uemail']).exists():
                return render(request, 'accounts/register.html', {"emalerr" : "sorry email already exist"})
            else:
                User.objects.create_user(username=request.POST['uname'], email=request.POST['uemail'], password=request.POST['upass'])
                return render(request, 'accounts/login.html')
        else:
            return render(request, 'accounts/register.html', {"perror": "mis match password"})
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        userchk = auth.authenticate(username=request.POST['uname'], password=request.POST['upass'])
        print(request.POST['uname'])
        print(request.POST['upass'])
        if userchk is not None:
            auth.login(request,userchk)
            return render(request,'products/home.html')
        else:
            return render(request, 'accounts/login.html',{"error": "invalid user name or password"})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'accounts/login.html')

