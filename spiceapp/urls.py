from django.urls import path
from . import views

app_name = 'spiceapp'

urlpatterns = [
   
    path('',views.index),
    path('login/',views.login, name='login'),
    path('signup',views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('view_product',views.view_product, name='view_product'),
    path('search/',views.search, name='search'),
    path('about',views.about, name='about'),
    
]