from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login, name='userlogin'),
    path('admin_login',views.admin_login, name='adminlogin')

]
