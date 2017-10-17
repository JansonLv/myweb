from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.


# 购物车
def cart(request):

    return render(request, 'carts/cart.html', locals())
