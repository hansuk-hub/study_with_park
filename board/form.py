from django import forms

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','password','username','content','photo']
        labels = {
            'title': '제목',
            'password' : '비밀번호',
            'username' : '글쓴이',
            'content': '내용',
            'photo' : '파일',

        }

