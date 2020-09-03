from django.db import models
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete

# Create your models here.

class Profile(models.Model):
    user = models.CharField(max_length=200)
    mob = models.IntegerField(max_length=12)
    
class Post(models.Model):
    title = models.CharField(max_length=120,default='')
    
    
def save_post(sender,instance,**kwargs):
    print("ok")
    
    
def save_pre(sender,instance,**kwargs):
    print("preee ok")
    
    
def save_delete(sender,instance,**kwargs):
    print("delete")
    
def saveee_delete(sender,instance,**kwargs):
    print("post_delete ")
    
post_save.connect(save_post,sender=Post)
pre_save.connect(save_pre,sender=Post)
pre_delete.connect(save_delete,sender=Post)
post_save.connect(saveee_delete,sender=Post)
