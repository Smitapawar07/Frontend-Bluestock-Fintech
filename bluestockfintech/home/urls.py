from home import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.adminlogin, name='login'),
    path('signin/', views.adminsignin, name='signin'),
    path('forgetpass/', views.adminforgetpass, name='forgetpass'),    
]
