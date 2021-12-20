from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from myadmin.models import *

def index(request):
    return render(request,"myadmin/index/index.html")

def login(request):
    '''加载登录页面'''
    return render(request,"myadmin/index/login.html")

def dologin(request):
    '''执行登录'''
    if request.method=="POST":
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        user=User.objects.filter(username=user,pwd=pwd).first()

        if user:
            juese=user.roles.all().values("permission__url")
            permisssion_list = []
            for item in juese:
                permisssion_list.append(item["permission__url"])
            print(permisssion_list)

            request.session['permisssion_list'] = permisssion_list
            request.session['adminuser'] = user.toDict()
            return redirect(reverse('myadmin_index'))

    return render(request,"myadmin/index/login.html")

def logout(request):
    '''执行退出'''
    del request.session['adminuser']
    return redirect(reverse('myadmin_login'))
...
...