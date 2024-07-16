from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('add/',add,name='add'),
    path('update/<int:id>/',update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
 ]