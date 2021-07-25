from django.shortcuts import render,get_object_or_404, redirect
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
    # post = get_object_or_404(Post, pk=post_id)
    # form = PostForm(instance=post)


    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.username = request.POST['username']
        post.title = request.POST['title']
        post.password = request.POST['password']
        post.content = request.POST['content']
        post.save()

        return HttpResponseRedirect(reverse('board:gotolist'))

        # form = PostForm(request.POST, instance=post)
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.username = request.username
        #     # question.modify_date = timezone.now()  # 수정일시 저장
        #     post.save()
        #     queryset = Post.objects.all()
        #
        #     return render(request, 'board/list.html', {
        #         'post_list': queryset
        #     })
    else:
        post = Post.objects.get(id=post_id)

        return render(request, 'board/update.html', {
            'post': post
        })
        # context = {'form': form}
        # return render(request, 'board/update.html', context)

def delete(request, post_id) :
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect( reverse('board:gotolist'))

def write(reqeust) :
    return render (reqeust, 'board/write.html')

