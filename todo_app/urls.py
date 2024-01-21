from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, NewLoginView, RegisterPage

urlpatterns = [
    path('', TaskList.as_view(), name='task'),
    path('task_create/', TaskCreate.as_view(), name='task_create'),
    path('login/', NewLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='tasks_detail'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='tasks_update'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='tasks_delete'),
]
