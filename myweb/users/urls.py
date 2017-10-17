from django.conf.urls import url
from .views import *

# ^起始字符一定要加,$结束符号根据要求
urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^info/$', info, name='info'),
    url(r'^order/$', order, name='order'),
    url(r'^site/$', site, name='site'),
    url(r'^deal_register/', deal_register, name='deal_register'),
]



