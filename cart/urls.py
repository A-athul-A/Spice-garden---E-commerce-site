from django.urls import path
from . import views

app_name = 'cartapp'

urlpatterns=[
    # path('add',views.add_cart,name='add_cart'),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:product_id>/',views.full_remove,name='full_remove'),

    path('add_buy/<int:product_id>/',views.add_buy,name='add_buy'),
    path('buy_detail',views.buy_detail,name='buy_detail'),
    path('buy_remove/<int:product_id>/',views.buy_remove,name='buy_remove'),
    path('buy_full_remove/<int:product_id>/',views.buy_full_remove,name='buy_full_remove'),
]