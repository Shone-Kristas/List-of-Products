from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import ShopList


# Create your views here.
def index(request):
    shops = ShopList.objects.order_by('id')
    return render(request, 'myapp/index.html', {'shop_list': shops, 'title': 'Главная страница'})



@require_http_methods(['POST'])
def add(request):
    name_add = request.POST['name_add']
    categ_add = request.POST['categ_add']
    cost_add = request.POST['cost_add']
    if name_add != '' and categ_add != '' and cost_add != '':
        shop = ShopList(name=name_add, category=categ_add, price=cost_add)
        shop.save()
        return redirect('index')
    elif name_add == '' or categ_add == '' or cost_add == '' or name == int:
        return redirect('index')

@require_http_methods(['POST'])
def update(request, shop_id):
    shop = ShopList.objects.get(id=shop_id)
    if request.POST['name_update'] == '':
        shop.name = shop.name
    else:
        shop.name = request.POST['name_update']
    if request.POST['categ_update'] == '':
        shop.category = shop.category
    else:
        shop.category = request.POST['categ_update']
    if request.POST['cost_update'] == '':
        shop.price = shop.price
    else:
        shop.price = request.POST['cost_update']
    shop.save()
    return redirect('index')

def delete(request, shop_id):
    shop = ShopList.objects.get(id=shop_id)
    shop.delete()
    return redirect('index')


def sorting_max_cost(request):
    queryset = ShopList.objects.order_by('-price')
    return render(request, 'myapp/index.html', {'shop_list': queryset, 'title': 'Главная страница'})

def sorting_min_cost(request):
    queryset = ShopList.objects.order_by('price')
    return render(request, 'myapp/index.html', {'shop_list': queryset, 'title': 'Главная страница'})

def sorting_min_numb(request):
    queryset = ShopList.objects.order_by('id')
    return render(request, 'myapp/index.html', {'shop_list': queryset, 'title': 'Главная страница'})

def sorting_max_numb(request):
    queryset = ShopList.objects.order_by('-id')
    return render(request, 'myapp/index.html', {'shop_list': queryset, 'title': 'Главная страница'})
@require_http_methods(['POST'])
def filter_cost(request):
    min_cost_html = request.POST['min_cost']
    max_cost_html = request.POST['max_cost']
    if min_cost_html != '' and max_cost_html != '':
        queryset = ShopList.objects.filter(price__range=(min_cost_html, max_cost_html))
        outset = queryset.order_by('price')
        return render(request, 'myapp/index.html', {'shop_list': outset, 'title': 'Главная страница'})
    elif min_cost_html != '' and max_cost_html == '':
        queryset = ShopList.objects.filter(price__gt=min_cost_html) # больше или равен
        outset = queryset.order_by('price')
        return render(request, 'myapp/index.html', {'shop_list': outset, 'title': 'Главная страница'})
    elif min_cost_html == '' and max_cost_html != '':
        queryset = ShopList.objects.filter(price__lte=max_cost_html) # меньше или равен
        outset = queryset.order_by('price')
        return render(request, 'myapp/index.html', {'shop_list': outset, 'title': 'Главная страница'})
    else:
        return redirect('index')