from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .functions import *
from .models import *
# Create your views here.





def login(request):
    return render(request, 'users/login.html', locals())


def register(request):
    error_mess = get_message(request)

    return render(request, 'users/register.html', locals())

# 用户中心-个人信息
def info(request):
    return render(request, 'users/user_center_info.html', locals())


# 用户中心-订单中心
def order(request):
    return render(request, 'users/user_center_order.html', locals())


# 用户中心 -收货地址
def site(request):
    return render(request, 'users/user_center_site.html', locals())


# 处理登录信息
def deal_register(request):
    #　判断资料是否符合情况
    if check_register_param(request):
        # 符合情况,加入数据库
        User.objects.user_registerData_save(request)
        print('注册成功')
        return redirect(reverse('users:login'))
    else:
        # 不符合情况,跳转回注册界面
        print('注册不成功')
        return redirect(reverse('users:register'))


