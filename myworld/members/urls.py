from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'), 
    path('add/addrecord/', views.addrecord, name='addrecord'), 
    path('delete/<int:id>', views.delete, name='delete'), 
    path('test/', views.testing , name='testing'),
    path('block/', views.block, name='block'),
    path('page/', views.page, name='page')
]