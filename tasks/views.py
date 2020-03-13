from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
import logging

from .models import * 
from .forms import *

logger = logging.getLogger(__name__)
# Create your views here.

def updateTask(request,pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance = task)
    logger.warning(form)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}

    return render(request,'tasks/update_task.html',context)

def deleteTask(request,pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'item':task.title}
    return render(request,'tasks/delete_task.html',context)

def userRegister(request):
    form = UserCreationForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username = username,password=password)
            login(request,user)
            return redirect('/')
        else:
            return render(request,'tasks/register.html',context)
    else:
        return render(request,'tasks/register.html',context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        if user:
            login(request,user)
        return redirect('/')
    else:
        return render(request,'tasks/login.html')

# def index(request):
#     logger.warning(request.user.is_authenticated)
#     if request.user.is_authenticated:
#         tasks = Task.objects.all()
#         form = TaskForm()
#         if request.method == 'POST':
#             form = TaskForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             return redirect('/')
#         context = { 'tasks' : tasks, 'form': form , 'User':User}
#         return render(request,'tasks/list.html',context)
#     else:
#         return redirect('/login')
    
def index(request):
    if request.user.is_authenticated:
        return redirect('/items')
    else:
        return redirect('/login')

def viewItems(request):
    if request.user.is_authenticated:
        return render(request,'tasks/itemList.html',{'items':Product.objects.all()})
    else:
        return redirect('/login')

def viewItemInfo(request,pk):
    logger.warning(Product.objects.get(id=pk))
    if request.user.is_authenticated:
        if request.method == 'POST':
            model = Cart.objects.create(item = Product.objects.get(id=pk),user=request.user)
            form = CartForm(instance=model)
            # if form.is_valid():
            new_obj = form.save(commit=False)
            new_obj.user = request.user
            new_obj.item = Product.objects.get(id=pk)
            new_obj.save()
            return redirect('/items')
        return render(request,'tasks/itemDetails.html',{'item':Product.objects.get(id=pk)})
    else:
        return redirect('/login')


def userCart(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            return redirect('/items')
        context : {'item':item}
        p= []
        for c in Cart.objects.all():
            if c.user.id == request.user.id:
                p.append(Product.objects.get(id=c.item.id))
        return render(request,'tasks/myCart.html',{'items':p})
    else:
        return redirect('/login')