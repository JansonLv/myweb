from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.


# 首页
def index(request):
    return render(request, 'goods/index.html', locals())


# 商品详情
def detail(request):

    return render(request, 'goods/detail.html', locals())


# 商品列表
def goods_list(request):
    return render(request, 'goods/list.html', locals())
