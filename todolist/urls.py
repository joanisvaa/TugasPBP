from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task, show_data_json, create_task_modal

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('create-task/', create_task, name='create_task'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_data_json, name='show_data_json'),
    path('add/', create_task_modal, name='create_task_modal'),
]
