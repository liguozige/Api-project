from django.shortcuts import render, get_object_or_404
from Api_app.models import *
import time
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
import json
from django.contrib.auth.decorators import login_required


# Create your views here.
def v_help(request):
    return render(request,'v_help.html')


# 登录页面
def login(request,message=''):
    res = {}
    res['notices'] = list(DB_notice.objects.all().values('content'))[::-1][0:2]
    res['message'] = message
    return render(request, 'login.html', res)


@login_required()
def index(request):
    return render(request,'index.html')


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
        # 去数据库中注册
        user = User.objects.create_user(username=username,password=password)
        # 成功，存储在数据库中，并登录，登陆后跳转到首页
        user.save()
        auth.login(request,user)
        request.session['user'] = username
        return HttpResponseRedirect('/index/')
    except:  # 失败，捕获异常，并返回登录页面
        return login(request,'用户名已存在')


# 获取统计数据
def get_tj_datas(request):
    # 获取用户Id
    userID = request.user.id
    tj_datas={}
    tj_datas["notices"]=list(DB_notice.objects.all().values('content'))[::-1]
    tj_datas["news"] = list(DB_news.objects.filter(to_user_id=userID).values())[::-1]
    tj_datas["overview"] = {
        "project_count":80,
        "api_count":30,
        "case_count":60,
        "env_count":45,
        "user_count":500
    }
    tj_datas["monitor"] = {
        "case_pass":70,
        "api_pass":65,
        "case_fail":24
    }
    tj_datas["contribution"] = {
        "project":50,
        "case":22,
        "api":74,
        "monitor":38,
        "case_run":44
    }
    return HttpResponse(json.dumps(tj_datas),content_type='application/json')


# 获取实时数据
def get_real_time_datas(request):
    real_time_datas = {
        "ApiShop_count":90,
        "UnReadNews_count":20,
        "RunCase_count":45,
        "Import_count":33
    }
    return HttpResponse(json.dumps(real_time_datas),content_type="application/json")


# 退出
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


# 获取项目列表数据
def get_project_list(request):
    keys = request.GET.get('keys',None)
    if keys:
        project_list_data = list((DB_project_list.objects.filter(name__contains=keys)|DB_project_list.objects.filter(des__contains=keys)).values())[::-1]
    else:
        project_list_data = list(DB_project_list.objects.filter(deleted=False).values())[::-1]
    # 增加字段
    for i in project_list_data:
        try:
            creater_name = get_object_or_404(User,pk = i['creater']).username
        except:
            creater_name = "未知用户"
        i["creater_name"] = creater_name
    return HttpResponse(json.dumps(project_list_data),content_type='application/json')


# 新增项目
def add_project(request):
    uid = request.user.id if request.user.id else 0
    DB_project_list.objects.create(creater=uid,des='默认描述')
    return get_project_list(request)


# 删除项目
def delete_project(request):
    project_id = request.GET['project_id']
    DB_project_list.objects.filter(id=project_id).update(deleted=True)
    return get_project_list(request)


# 获取单个项目详情
def get_project_detail(request):
    id = request.GET['id']
    form = list(DB_project_list.objects.filter(id=id).values())[0]
    return HttpResponse(json.dumps(form),content_type="application/json")


# 保存项目
def save_project(request):
    form = json.loads(request.body.decode('utf-8'))
    # DB_project_list.objects.filter(id=form['id']).update(name=form['name'], des=form['des'])
    DB_project_list.objects.filter(id=form['id']).update(**form)
    return HttpResponse(form, content_type="application/json")
