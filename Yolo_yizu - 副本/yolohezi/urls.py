from django.urls import path
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/yolohezi/login/
    path('login/', views.login, name='login'),
    #http://127.0.0.1:8000/yolohezi/logout/
    path('logout/', views.logout, name='logout'),
]
