from django.urls import path
from .views import index, gotolist, write


urlpatterns = [
    path('',index,name='index'),
    path('list/', gotolist, name='gotolist'),
    path('write/', write, name='write'),
    path('gotolist/', gotolist, name='gotolist')



]