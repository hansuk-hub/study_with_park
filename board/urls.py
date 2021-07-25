from django.urls import path
from .views import index, gotolist, write, postCreate, update,delete


urlpatterns = [
    path('',index,name='index'),
    path('list/', gotolist, name='gotolist'),
    path('postCreate/', postCreate, name='postCreate'),
    path('write/', write, name='write'),
    path('gotolist/', gotolist, name='gotolist'),
    path('update/<int:post_id>', update, name='update'),
    path('delete/<int:post_id>', delete, name='delete'),

]