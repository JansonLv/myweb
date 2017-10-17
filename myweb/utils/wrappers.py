from django.contrib import messages
import hashlib

def post_getvalue(request, key):
    return request.POST.get(key, None).strip()


def get_getvalue(request, key):
    return request.GET.get(key, None).strip()

# 增加消息到系统消息队列中,调用时利用spilt切割
def add_message(request, key, mess):
    messages.add_message(request, messages.INFO, key+':'+mess)

# 取出所有错误信息并整理返回
def get_message(request):

    # 取出所有错误信息
    mess = messages.get_messages(request)
    # print(mess)
    info = dict()
    for message in mess:
        messaage_list = str(message).split(':')
        info[messaage_list[0]] = messaage_list[1]

    return info

# 加密数据
def password_encryption(password, salt=''):
    sha = hashlib.sha256()
    new_password = '$%^$%^@$%@' + password + salt + '*(&^%$#DSFGDRS'
    sha.update(new_password.encode('utf-8'))

    return sha.hexdigest()
