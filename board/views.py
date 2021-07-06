from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1> Hello </h1>')

def gotolist(request) :
    username = request.POST.get('username','')
    userpwd = request.POST.get('password','')
    usertitle = request.POST.get('usertitle', '')
    usercontent = request.POST.get('usercont', '')

    return render(request, 'list.html', {'username':username, 'userpwd': userpwd, 'usertitle': usertitle, 'usercontent' :usercontent })

def write(reqeust) :
    return render (reqeust, 'write.html')

