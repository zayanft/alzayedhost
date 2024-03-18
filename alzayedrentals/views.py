from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    obj = home_slide.objects.all()
    context = {
        'obj': obj
        }
    return render(request, 'index.html',context)



def service(request):
    services_list = Service.objects.all()
    context = {
        'services_list':services_list
    }
    return render(request, "service/index.html",context)

def about(request):
    
    return render(request,'about/index.html')

def equipment(request):
    category = request.GET.get('category')
    
    if category == None:
        products = Equipment.objects.all()

    else:
        products = Equipment.objects.filter(category__name=category)




    categories = Category.objects.all()
    
    context = {
        'products':products,
        'categories':categories
    }
    
    return render(request, 'equipment/index.html',context)

def contact(request):
    
    return render(request,'contact/index.html')