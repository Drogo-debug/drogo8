from . import views
from django.urls import path, include
from .views import UserFormView




urlpatterns =[
    path('',views.home,name='home'),
    path('login/',views.loging, name='login'),
    path('register/',views.register,name='register'),
    path('back/',views.back,name='back'),
    path('landing/', UserFormView.as_view(), name='user_form')
    ]