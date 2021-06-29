from django.urls import path
from .views import index, list


urlpatterns = [
    path('',index),
    path('list/', list )
]