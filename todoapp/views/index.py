from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import  View
from django.contrib.sessions.models import Session
from todoapp.models.users import User
from todoapp.models.todo import TODO

def index(request):
    user = request.session.get('user')
    print(user)
    if not user:
        return render(request,'index.html')
    email = request.session['email']
    user = User.get_user_by_email(email)
    data = {
        'firstname':user.first_name,
    }
    return render(request,'index.html',data)

def mytodo(request):
    user = request.session.get('user')
    print(user)
    if not user:
        return redirect('login')
    email = request.session['email']
    user = User.get_user_by_email(email)
    todos = TODO.objects.filter(user = user).order_by('priority')
    data = {
        'todos':todos,
        'firstname':user.first_name,
    }
    return render(request,'mytodo.html',data)



def add_todo(request):
    user = request.session.get('user')
    print(user)
    if not user:
        return render(request,'index.html')
    email = request.session['email']
    user = User.get_user_by_email(email)
    title = request.POST.get('title')
    status = request.POST.get('status')
    priority = request.POST.get('priority')
    error_message=None
    if int(priority)>=1 and int(priority)<=10:
        error_message=None
    else:
        error_message="Invalid Priority!!!"
    if user and not error_message:
        todo =  TODO(title=title,
                    status=status,
                    priority=priority,
                    user=user) 
        todo.save()
        print(todo)
        return redirect("mytodo")
    else:
        todos = TODO.objects.filter(user = user).order_by('priority')
        data = {
            'todos':todos,
            'firstname':user.first_name,
            'error':error_message,
        } 
        return render(request , 'mytodo.html' , context=data)


def delete_todo(request , id ):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('mytodo')

def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('mytodo')
