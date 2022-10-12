from django.shortcuts import render
from todolist.models import Task, CreateTask
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required(login_url = '/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
    'list_task': data_task,
    }

    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist:login')
    
    context = {'form':form}
    
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'username atau password salah!')
    context = {}
    return render(request, 'login.html', context)

def create_task(request):
    form = CreateTask()

    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('todolist:show_todolist')

    context = {
        'form' : form
    }
    return render(request, "create_task.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def show_data_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_task_modal(request):

    if request.method == 'POST':
        title = request.POST.get('task_title')
        description = request.POST.get('task_desc')
        task =  Task.objects.create(task_title=title, task_description=description,task_date=datetime.date.today(), user=request.user)

        new_task = {
                'title':task.task_title,
                'description':task.task_description,
                'date':task.task_date,
        }

        return JsonResponse(new_task)
