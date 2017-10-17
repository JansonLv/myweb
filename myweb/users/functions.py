from utils.wrappers import *
import re
from .models import *



def check_register_param(request):
    # 获取信息
    user_name = post_getvalue(request, 'user_name')
    user_pwd1 = post_getvalue(request, 'user_pwd1')
    user_pwd2 = post_getvalue(request, 'user_pwd2')
    user_email = post_getvalue(request, 'user_email')
    user_allow = post_getvalue(request, 'user_allow')

    flag = True

    if User.objects.get_userData_by_name(user_name):
        add_message(request, 'user_name', '用户名已存在')
        return False

    # 判断用户名长度是否符合,
    if not (16 > len(user_name) > 5):
        add_message(request, 'user_name', '用户名长度不符合')
        flag = False

    # 密码长度
    if not (16 > len(user_pwd1) > 5 and re.match(r'^\w+$', user_name)):
        add_message(request, 'user_pwd1', '密码长度不符合且只能为字母和数字')
        flag = False

    # 密码相等
    if not (user_pwd1 == user_pwd2):
        add_message(request, 'user_pwd2', '两次密码要一样')
        flag = False

    # 判断邮箱符合规范
    reg = r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(reg, user_email):
        add_message(request, 'user_email', '邮箱不正确')
        flag = False

    # 是否同意协议
    if not(user_allow == 'on'):
        add_message(request, 'user_allow', '请阅读协议')
        flag = False

    return flag



