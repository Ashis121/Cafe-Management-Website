from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request,'pages/index.html')
def about(request):
    students= {'Tom':80,'Jerry':50,'Casper':40}
    context ={
        'students':students,
        
    }
    return render(request,'pages/about.html',context)
def contact(request):
    return render(request,'pages/contact.html')
