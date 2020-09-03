from django.shortcuts import render , get_object_or_404 , redirect
from .forms import ProductForm , RawProductForm
from django.http import Http404

from . models import Product

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {}
    context['title'] = obj.title
    context['desc'] = obj.description
    return render(request,'products/details.html',context)


def product_create_view(request):
    """
    This is Class FORM  
    """
    form = ProductForm(request.POST or None)
    # if request.method == 'POST':
    if form.is_valid():
        form.save()
    context = {  }
    context['form'] = form
    return render(request,"products/create.html",context)


# def product_create_view(request):
#     """
#     This is The RAW FROM
#     """
#     if request.method == "POST":
#         title = request.POST.get('title')
#         price = request.POST.get('price')

#         Product.objects.create(title=title,price=price)
#     context = {}
#     return render(request,"products/create.html",context)



# def product_create_view(request):
#     """
#        This is  ROW Form
#     """
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#     form = RawProductForm()
#     context = {'form' : form}
#     return render(request,"products/create.html",context)


def render_initial_data(request,id):
    initial_data =  {
        "title" : "My This Awesome"
    }
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    context = {
         "form" : form
    }
    return render(request,"products/create.html",context)


def dynamic_lookup_view(request,id):
    try:
        obj = get_object_or_404(Product,id=id)
    except Product.DoesNotExist:
        raise Http404()
    
    context = { "object" : obj }
    return render(request,"products/details.html",context)

def product_delete_viiew(request,id):
    try:
        obj = get_object_or_404(Product,id=id)
        if request.method == "POST":
            obj.delete()
            # redirect('delete')
        context = { "object" : obj }
        return render(request,"products/delete.html",context)
    except Product.DoesNotExist:
        raise Http404()


def product_update_view(request,id):
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST or None , instance=obj)
    print(request.POST)
    if form.is_valid():
        form.save()
    context = { "form" : form }
    return render(request,"products/create.html",context)





def product_list_view(request):
    objects = Product.objects.all()
    context = { "objects" : objects }
    return render(request,"products/list.html",context)
