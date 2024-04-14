from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_home),
    path('task/task_list', views.task_list, name="task_list"),
    path('task/create_task', views.create_task ,name="create_task"),
    path('task/delete/<int:task_id>/', views.delete_task ,name="delete_task"),
    path('task/delete_all_task', views.delete_all_tasks ,name="delete_all_task"), 
    path('task/edit/<int:task_id>/', views.edit_task ,name="edit_task"),
    path('task/detail/<int:task_id>/', views.detail_task ,name="detail_task"),
    
    path('users/users_list', views.user_list, name="user_list"),
    path('users/create_users', views.create_user ,name="create_user"),
    path('users/delete/<int:user_id>/', views.delete_user ,name="delete_user"),
    path('users/delete_all_users', views.delete_all_users ,name="delete_all_user"), 
    path('users/edit/<int:user_id>/', views.edit_user ,name="edit_user"),
    path('users/detail/<int:user_id>/', views.detail_user ,name="detail_user"),
]
