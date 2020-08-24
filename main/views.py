from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Todo

# Create your views here.

def home(request):
	todo_items=Todo.objects.all().order_by("-added_date")
	context= {"todo_items": todo_items}

	return render(request, 'main/index.html', context)

@csrf_exempt
def add_todo(request):
	current_date=timezone.now()
	content = request.POST["content"]
	created_obj = Todo.objects.create(added_date=current_date, text=content)
	length_of_todos = Todo.objects.all().count()
	return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request, todo_id):
	Todo.objects.get(id=todo_id).delete()
	return HttpResponseRedirect('/')