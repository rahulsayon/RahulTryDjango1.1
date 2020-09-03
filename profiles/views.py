from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver , Signal
from .models import Post
# Create your views here.
mysignal = Signal(providing_args=['name'])

def get_data(request):
    mysignal.send(sender=Post,name='Mohan')
    return HttpResponse("Hi, All How rae You !!!!")


@receiver(request_finished)
def getall(sender,**kwargs):
    print("Request Fineshed")
    
@receiver(mysignal)
def all(sender,**kwargs):
    print("allllllllllllllllllllll")