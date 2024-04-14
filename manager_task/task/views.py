from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, User
# Create your views here.


def get_home(req):  
    return render(req,'task/base.html')


def task_list(req):
    todos = Job.objects.all()
    return render(req,'task/index.html' , {'tasks':todos})


# model -> view -> trả dữ liệu về cho người dùng

def user_list(req):
    td = User.objects.all()
    return render(req,'user/list_user.html' , {'td':td})

def create_task(req):
    if req.method == 'POST':
        name_job = req.POST.get("name_job")
        describe = req.POST.get("describe")
        Job.objects.create(job_name = name_job, describe = describe)
        return redirect('task_list')
    return render(req, 'task/create_task.html' )


def create_user(req):
    todos = Job.objects.all()
    if req.method == 'POST':
        user_name = req.POST.get("user_name")
        school_name = req.POST.get("school_name")
        address =req.POST.get("address")
        selected_job_id = req.POST.get("task")
        job = Job.objects.get(id=selected_job_id)
        User.objects.create(user_name=user_name, school_name=school_name, address=address, job = job)
        
       
        return redirect('user_list')
    return render(req, 'user/create_user.html' , locals())


def delete_task(req ,task_id):
    todo = Job.objects.get(id=task_id)
    todo.delete()
    return redirect('task_list')


def delete_user(req ,user_id):
    todo = User.objects.get(id=user_id)
    todo.delete()
    return redirect('user_list')

def edit_task(req, task_id):
    todo = Job.objects.get(id = task_id)
    if req.method=='POST':
        name_job = req.POST.get("name_job")
        describe = req.POST.get("describe")
        todo.job_name = name_job
        todo.describe = describe
        todo.save()
        return redirect('task_list')

    
    context = {'job_name': todo.job_name, 'describe': todo.describe,  "id": todo.id}
    return render(req, 'task/edit_task.html', context)
  
  
def edit_user(req, user_id):
    todos = Job.objects.all()
    todo = User.objects.get(id = user_id)
    if req.method=='POST':
        user_name = req.POST.get("user_name")
        school_name = req.POST.get("school_name")
        address =req.POST.get("address")
        selected_job_id = req.POST.get("task")
        job = Job.objects.get(id=selected_job_id)
        
        
        todo.user_name = user_name
        todo.school_name = school_name
        todo.address = address
        todo.job= job
        todo.save()
        return redirect('user_list')

    
    context = {'user_name': todo.user_name, 'school_name': todo.school_name, 'address': todo.address,'todos': todos, "id": todo.id}
    return render(req, 'user/edit_user.html', context)
  
  
def detail_task(req, task_id):
    todo = Job.objects.get(id = task_id)
    context = {'job_name': todo.job_name, 'describe': todo.describe,  "id": todo.id}
    return render(req, 'task/detail_task.html', context)

def detail_user(req, user_id):
    todos = User.objects.get(id = user_id)
    todo = Job.objects.get(id = user_id)
    context = {'user_name': todos.user_name, 'school_name': todos.school_name, 'address': todos.address, 'job' : todos.job.job_name, "id": todos.id}
    return render(req, 'user/detail_user.html', context)

def delete_all_tasks(req):
    Job.objects.all().delete()
    return redirect('task_list')
def delete_all_users(req):
    User.objects.all().delete()
    return redirect('user_list')