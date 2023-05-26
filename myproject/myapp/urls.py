from django.urls import path
from myapp import views
from .views import *

urlpatterns = [
    path('items',views.items_list,name='items'),
    path('items/<int:id>',views.item_func,name='item_func')
    ]