
from django.urls import path

from account import views

urlpatterns = [

    path('login/', views.login, name='signin'),
    path('register/', views.register, name='signup'),
    path('logout/', views.logout, name='logout'),

]
