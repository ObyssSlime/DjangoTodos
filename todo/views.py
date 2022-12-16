from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Todo

# Create your views here.
def index(request):
    items = Todo.objects.order_by('-id')
    return render(request, 'todo/index.html', {'items': items})

def create(request):
    try:
        title = request.POST['title']
        todo = Todo(title=title)
        todo.save()
        return HttpResponseRedirect(reverse('index'))
    except Exception:
        return HttpResponseRedirect(reverse('index'))

def update(request, id):
    todo = Todo.objects.get(id=id)
    todo.status = not todo.status
    todo.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    delete = Todo.objects.get(id=id)
    delete.delete()
    return HttpResponseRedirect(reverse('index'))

def delete_all(request):
    delete_all = Todo.objects.all()
    delete_all.delete()
    return HttpResponseRedirect(reverse('index'))

def pending(request):
    pending = Todo.objects.filter(status=False).order_by('-id')
    return render(request, 'todo/index.html', {'items': pending})

def done(request):
    done = Todo.objects.filter(status=True).order_by('-id')
    return render(request, 'todo/index.html', {'items': done})
