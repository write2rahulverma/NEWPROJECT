from django.shortcuts import render, redirect
from django .contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from NEWAPP.forms import *
from NEWAPP.models import *

def show(request):
    products = Product.objects.all()
    return render(request, "show.html",{'products':products})

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/register')
    else:
        return redirect('/register')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Exists')
                return redirect('/register#toregister')
            else:
                user = User.objects.create(username=username, password=password, firstname=first_name, lastname=last_name)
                user.save()
                messages.success(request,'User Created')
                return redirect('/register')
        else:
            messages.error(request,'Password does not matched')
            return redirect('/register#toregister')
    else:
        return render(request,"register.html")

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
