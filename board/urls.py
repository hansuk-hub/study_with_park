from django.urls import path
from .views import index, gotolist, write, postCreate


urlpatterns = [
    path('',index,name='index'),
    path('list/', gotolist, name='gotolist'),
    path('postCreate/', postCreate, name='postCreate'),
    path('write/', write, name='write'),
    path('gotolist/', gotolist, name='gotolist')



]