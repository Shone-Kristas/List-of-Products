from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<int:shop_id>/', views.delete, name='delete'),
    path('update/<int:shop_id>/', views.update, name='update'),
    path('sortingmincost', views.sorting_min_cost, name='sortingmincost'),
    path('sortingmaxcost', views.sorting_max_cost, name='sortingmaxcost'),
    path('sortingminnumb', views.sorting_min_numb, name='sortingminnumb'),
    path('sortingmaxnumb', views.sorting_max_numb, name='sortingmaxnumb'),
    path('filtercost', views.filter_cost, name='filtercost'),
]