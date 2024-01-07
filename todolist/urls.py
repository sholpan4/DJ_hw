from django.urls import path
from .views import *

app_name = 'todolist'

urlpatterns = [
    path('todolist/get/', get_all_tasks, name='get_all_tasks'),
    path('todolist/get_task/', get_task, name='get_task'),
    path('todolist/create/', create_task, name='create_task'),
    path('todolist/update/', update_task, name='update_task'),
    path('todolist/delete/', delete_task, name='delete_task'),
]