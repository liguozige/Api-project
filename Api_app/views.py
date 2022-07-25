from django.shortcuts import render
from Api_app.models import *
import time
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def v_help(request):
    return render(request,'v_help.html')

# 登录页面
def login(request,message=''):
    res={}
    res['notices'] = list(DB_notice.objects.all().values('content'))[::-1][0:2]
    res['message'] = message
    return render(request, 'login.html', res)

# 登录功能
def login_action(request):
    time.sleep(1)
    # 获取用户名/密码
    username = request.POST.get('username',None)
    password = request.POST.get('password',None)
    # 去数据库中判断
    user = auth.authenticate(username=username,password=password)
    if user is None:  # 比对失败，跳转到登录页面
        return login(request,'用户名或密码错误')
    else:  # 比对成功，登录
        auth.login(request,user)
        request.session['user'] = username
        # 跳转到首页
        return HttpResponseRedirect('/index/')  # 此页面还没写，先填写help吧

# 注册功能
def register_action(request):
    time.sleep(1)
    # 获取用户名/密码
    username = request.GET['username']
    password = request.GET['password']
    try:
        #去数据库中注册
        user = User.objects.create_user(username=username,password=password)
        # 成功，存储在数据库中，并登录，登陆后跳转到首页
        user.save()
        auth.login(request,user)
        request.session['user'] = username
        return HttpResponseRedirect('/index/')
    except:# 失败，捕获异常，并返回登录页面
        return login(request,'用户名已存在')