
from django.urls import path
from .views import *

app_name = 'testapp'

urlpatterns = [
    path('/login_page/', protected_view, name='protected_view'),
    path('', index, name='index'),
]
