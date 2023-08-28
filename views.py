import datetime

from django.shortcuts import render, redirect
from .models import TableTask
from django.http import HttpResponse


def table_task_view(request):
    tasks = TableTask.objects.all()
    return render(request, 'table_task.html', {'tasks': tasks})


def unready_table_view(request):
    tasks = TableTask.objects.filter(stage='На выводе')
    return render(request, 'unready_table.html', {'tasks': tasks})


def ready_table_view(request):
    tasks = TableTask.objects.filter(stage='Готово')
    return render(request, 'ready_table.html', {'tasks': tasks})


def update_stage_view(request, task_id):
    if request.method == 'POST':
        task = TableTask.objects.get(id=task_id)
        task.stage = 'Готово'
        task.ready_date_time = datetime.datetime.now()
        task.save()
        return redirect('table_task')

    return HttpResponse("Invalid request")
