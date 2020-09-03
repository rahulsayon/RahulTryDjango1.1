from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Course
from courses.forms import CourseModelForm 
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
# class CourseView(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,'course/about.html',{})

# def fav(request,*args,**kwargs):
#     return render(request,"about.html",{})


# Create your views here.



class CourseObjectMixin(object):
    model = Course
    lookup = 'id'
    
    """
        get_objects and get_queryset two methos is there
    """
    
    def get_objects(self):
        id = self.kwargs.get('id')
        obj = None
        if obj is not None:
            obj = get_object_or_404(self.model,id=id)
        return obj


class CourseView(CourseObjectMixin,View):
    def get(self,request,id=None,*args,**kwargs):
        print("idddddddddddddddddddddddddd",id)
        if id is not None:
            obj = get_object_or_404(Course,id=id)
            print("objobjobjobjobj",obj)
            context = { "object" : obj }
        return render(request,'courses/details.html',context)

class CourseListView(View):
    queryset = Course.objects.all()
    def get_queryset(self):
        return self.queryset

    def get(self,request,*args,**kwargs):
        context = { "object_list" : self.get_queryset()  }
        return render(request,"courses/list.html",context)



class CourseCreateView(View):
    def get(self,request,*args,**kwargs):
        form = CourseModelForm()
        context = { "form" : form }
        return render(request,"courses/create.html",context)

    def post(self,request,*args,**kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
        context = { "form" : form }
        return render(request,"courses/create.html",context)
    


class CourseUpdateView(View):
    def get_object(self):
        context = {}
        id_ = self.kwargs.get('id')
        if id_ is not None:
            obj = get_object_or_404(Course,id=id_)
            context['object'] = obj
        return obj
            
            
    def get(self,request,id=None,*args,**kwargs):
        obj = self.get_object()
        form = CourseModelForm(instance=obj)
        context = { "form" : form }
        return render(request,"courses/update.html",context)

    def post(self,request,*args,**kwargs):
        obj= self.get_object()
        form = CourseModelForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        context = { "form" : form }
        return render(request,"courses/update.html",context)
    
    
    
class CourseDeleteView(View):
    def get_object(self):
        context = {}
        id_ = self.kwargs.get('id')
        if id_ is not None:
            obj = get_object_or_404(Course,id=id_)
            context['object'] = obj
        return obj
            
            
    def get(self,request,id=None,*args,**kwargs):
        obj = self.get_object()
        context = { "object":obj }
        return render(request,"courses/delete.html",context)

    def post(self,request,id=None,*args,**kwargs):
        obj= self.get_object()
        if obj is not None:
            obj.delete()
            return redirect('/course/')
        context = {  }
        return render(request,"courses/delete.html",context)
    
    

def sendemail(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['rahulsayon95@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/course/')