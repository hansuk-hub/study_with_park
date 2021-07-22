from django.db import models

class Post(models.Model) :
    title = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add= True)
    modified_datetime = models.DateTimeField(auto_now = True)
    likes = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='post/%Y%m%d')



class Comment(models.Model) :
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    username = models.CharField(max_length= 100)
    password = models.CharField(max_length = 100)
    modified_datetime = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)


class Tag(models.Model) :
    name =models.CharField(max_length=20)