from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .form import PostForm
from .models import *

# Create your views here.
def index(request):
    return HttpResponse('<h1> Hello </h1>')


def gotolist(request) :
    queryset = Post.objects.all()

    return render ( request, 'board/list.html', {
        'post_list' : queryset
    })


def postCreate(request) :
    username = request.POST.get('username','')
    userpwd = request.POST.get('password','')
    usertitle = request.POST.get('usertitle', '')
    usercontent = request.POST.get('usercont', '')
    photo = request.FILES.get('photo')
    new_post = Post(title=usertitle, username = username, password = userpwd, content = usercontent, photo = photo)
    new_post.save()
    return HttpResponseRedirect( reverse('board:gotolist'))


def update(request, post_id) :
    question = get_object_or_404(Post, pk=post_id)
    form = PostForm(instance=question)
    context = {'form': form}

    return render(request, 'board/update.html', context)



def write(reqeust) :
    return render (reqeust, 'board/write.html')

