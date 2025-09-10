from django.urls import path
from .views import home,login_view,signup_view,cities,logout_view
urlpatterns=[

path('',home,name='home'),
path('login/',login_view,name='login'),
path('signup/',signup_view,name='signup'),
path('cities/',cities,name='cities'),
path('logout/',logout_view,name='logout'),




]