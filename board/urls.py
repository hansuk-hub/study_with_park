from django.urls import path
from .views import index, list, write


urlpatterns = [
    path('',index,name='index'),
    path('list/', list, name='list'),
    path('write/', write, name='write'),



]