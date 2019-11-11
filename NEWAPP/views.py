from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from NEWAPP.forms import *
from NEWAPP.models import *

def show(request):
    products = Product.objects.all()
    return render(request, "show.html",{'products':products})

def index(request):
    return render(request,"index.html")

def registrationPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        user = User.objects.create_user(username=username, password=password, firstname=first_name, lastname=last_name)
        user.save()
        print('user created')
        return redirect('/')
        
    else:
        return render(request,"register.html")

def register(request):
    form = UserCreationForm
    return render(request,"register.html",context={"form":form})

def addData(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = ProductForm()
        return render(request,'index.html',{'form':form})

def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request,'edit.html',{'product':product})

def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance = product)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request,'edit.html',{'product':product})

def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/")
