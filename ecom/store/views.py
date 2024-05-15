from django.shortcuts import render,redirect
from . import views
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from .models import Category

cc=Category.objects.all()

# Create your views here.
def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products,'cc':cc})

def about(request):
    return render(request,'about.html',{'cc':cc})

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("you have been successfully logged In"))
            return redirect('home')
        else:
            messages.success(request,("username and passwords doesn't match! please try again"))
            return redirect('login')
    else:
        return render(request,'login.html',{'cc':cc})

def logout_user(request):
    logout(request)
    messages.success(request, ("thank you"))
    return redirect('home')

def register_user(request):
    form=SignUpForm()
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,("you have been successfully registered "))
            return redirect('home')
        else:
            messages.success(request,("OOPS!! there was a problem registering , please try again"))
            return redirect('register')
    else:
        return render(request,'register.html',{'form':form,'cc':cc})
    
def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product,'cc':cc})

from django.shortcuts import get_object_or_404

def category(request, varr):
    varr = varr.replace('-', ' ')
    category = get_object_or_404(Category, name=varr)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'products': products, 'category': category,'cc':cc})



