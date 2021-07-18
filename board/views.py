from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse('<h1> Hello </h1>')


def gotolist(request) :
    return render ( request, 'board/lsit.html')


def postCreate(request) :
    username = request.POST.get('username','')
    userpwd = request.POST.get('password','')
    usertitle = request.POST.get('usertitle', '')
    usercontent = request.POST.get('usercont', '')
    new_post = Post(title=usertitle, username = username, password = userpwd, content = usercontent)
    new_post.save()
    return HttpResponseRedirect( reverse('index'))


    title = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    content = models.TextField()





def write(reqeust) :
    return render (reqeust, 'board/write.html')

