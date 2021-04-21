from django.urls import path
from . import views

# Write your path here..

urlpatterns = [
    path('admin_login',views.admin_login,name="admin_login"),
    path('user_details',views.user_details,name="user_details"),
    path('add_user',views.add_user,name="add_user"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
    path('delete_user/<int:pk>',views.delete,name="delete_user"),
    path('update_user/<int:pk>',views.update,name="update_user"),
    # path('new_one',views.new,name="new_one")
    
]