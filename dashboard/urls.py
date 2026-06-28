from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('users/',views.users,name='users'),
    path('add-user/',views.adduser,name='add-user'),
    path('profile/',views.profile,name='profile'),
    path('charts/',views.charts,name='charts'),
    path('tables/',views.tables,name='tables'),
]