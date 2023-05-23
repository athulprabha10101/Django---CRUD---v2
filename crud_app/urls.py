from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login, name='userlogin'),
    path('admin_login',views.admin_login, name='adminlogin'),
    path('user_home',views.user_home, name='userhome'),
    path('admin_home',views.admin_home, name='adminhome'),
    path('signup',views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('add_user', views.add_user, name = 'add_user'),
    path('edit_details<int:id>', views.edit_details, name = 'edit_details'),
    path('update_details<int:id>', views.update_details, name = 'update_details'),
    path('delete_user<int:id>', views.delete_user, name = 'delete_user'),
    
]
