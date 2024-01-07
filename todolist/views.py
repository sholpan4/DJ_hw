import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from .models import Task


# def index(request):
#     return render(request)


def get_all_tasks(request):
    tasks = Task.objects.all()
    task_list = [{'id': task.id, 'title': task.title, 'description': task.description,
                  'completed': task.completed} for task in tasks]
    return JsonResponse({'task': task_list})


def get_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return JsonResponse({'id': task.id, 'title': task.title, 'description': task.description,
                         'completed': task.completed})


@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title', '')
        description = data.get('description', '')
        completed = data.get('completed', False)

        new_task = Task.objects.create(title=title, description=description, completed=completed)
        return JsonResponse({'id': new_task.id, 'title': new_task.title, 'description': new_task.description,
                             'completed': new_task.completed})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for creating tasks.'}, status=405)


@csrf_exempt
def update_task(request, task_id):
    task = get_object_or_404(Task, task_id)

    if request.method == 'PUT':
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.completed = data.get('completed', task.completed)
        task.save()

        return JsonResponse({'id': task.id, 'title': task.title, 'description': task.description,
                             'completed': task.completed})
    else:
        return JsonResponse({'error': 'Only PUT requests are allowed for updating tasks.'}, status=405)


@csrf_exempt
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully.'})
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed for deleting tasks.'}, status=405)