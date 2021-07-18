from django.db import models

class Post(models.Model) :
    title = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    content = models.TextField()

class Comment(models.Model) :
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

class Tag(models.Model) :
    name =models.CharField(max_length=20)git
