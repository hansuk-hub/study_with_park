from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1> Hello </h1>')

def list(request) :
    username = request.GET.get('username')
    userpwd = request.GET.get('password')
    usertitle = request.GET.get('usertitle')
    usercontent = request.GET.get('usercont')

    return render(request, 'list.html', {'username':username, 'userpwd': userpwd, 'usertitle': usertitle, 'usercontent' :usercontent })

def write(request) :
    return render(request, 'write.html')

