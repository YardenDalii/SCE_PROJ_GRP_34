from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
#   Created by Eshed Sorotsky
#   29/NOV/21
#the blogusers model, general for registered,editor & administrator
class bloguser(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20,default = '')
    password = models.CharField(max_length = 30)
    nickname = models.CharField(max_length = 20,default = '',null = True)
    email = models.EmailField(max_length = 50,unique = True)
    role = models.CharField(max_length = 10,default = 'registered',null = True)
    bio = models.CharField(max_length=300,default = "",null = True)
    created = models.DateTimeField(auto_now_add = True)
    #picture = models.ImageField(default = None,upload_to=None, height_field=None, width_field=None, max_length=100)

    class Meta:
        db_table = "bloguser"

#posts class
class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    tags = models.CharField(max_length = 250,default = None)
    #1 to many consisting of all the ratings
    ratings = models.ForeignKey('Rating',default = None,on_delete = models.CASCADE,null = True)
    #1 to many consisting of all the comments of a certain post
    comments = models.ForeignKey('Comment',default = None,on_delete=models.CASCADE,null = True)
    #1 to 1 relation for the post owner
    owner = models.ForeignKey('bloguser',default = None,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    class Meta:
        db_table = "post"

#comments class
class Comment(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField(max_length = 100)
    #1 to 1 relation for the comment owner
    owner = models.ForeignKey('bloguser',default = None,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    class Meta:
        db_table = "Comment"

#Rating class
class Rating(models.Model):
    star = models.DecimalField(max_digits = 1,decimal_places = 1)
    #created = models.DateTimeField(auto_now_add = False)
    class Meta:
        db_table = "Rating"

#become editor requests
class become_editor_model(models.Model):
    requested_by = models.ForeignKey('bloguser',default = None,on_delete = models.CASCADE,null = True)
    content = models.CharField(max_length=300,default = None)
    class Meta:
        db_table = "become_editor_model"