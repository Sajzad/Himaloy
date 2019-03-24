from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField

User=get_user_model()


class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture= models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title=models.CharField(max_length=40)


    def __str__(self):
        return self.title

# Course Overview

class CourseOverview(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    categories= models.ForeignKey(Category, on_delete= models.CASCADE)
    overview= models.TextField()

    def __str__(self):
        return self.user.username



class Post(models.Model):
    title=models.CharField(max_length=100)
    overview=models.TextField()
    content= HTMLField(default='content')
    timestamp=models.DateTimeField(auto_now_add=True)
    comment_count=models.IntegerField(default=0)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    thumbnail=models.ImageField()
    categories= models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    featured=models.BooleanField()
    previous_post= models.ForeignKey('self', related_name= 'previous', on_delete= models.CASCADE, blank=True, null=True)
    next_post= models.ForeignKey('self', related_name= 'next', on_delete= models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs=
                                    { 'id': self.id
                                    })


    @property
    def get_comments(self):
        return self.comment.all().order_by(-timestamp)



class Signup(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email


class Comment(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    content= models.TextField()
    post_comment=models.ForeignKey(Post, related_name='comment', on_delete= models.CASCADE)

    def __str__(self):
        return self.user.username




# Create your models here.
