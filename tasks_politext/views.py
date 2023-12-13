import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import LoginForm
from .models import TableTask


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('table_task')  # перенаправить на вашу домашнюю страницу
        else:
            # обработка некорректного входа
            return render(request, 'login.html', {'error_message': 'Неверное имя пользователя или пароль'})
    else:
        return render(request, 'login.html')


@login_required
def table_task_view(request):
    tasks = TableTask.objects.all()
    return render(request, 'table_task.html', {'tasks': tasks})

@login_required
def unready_table_view(request):
    tasks = TableTask.objects.filter(stage='На выводе')
    return render(request, 'unready_table.html', {'tasks': tasks})

@login_required
def ready_table_view(request):
    tasks = TableTask.objects.filter(stage='Готово')
    return render(request, 'ready_table.html', {'tasks': tasks})


@login_required
def update_stage_view(request, task_id):
    if request.method == 'POST':
        try:
            task = TableTask.objects.get(id=task_id)
            task.stage = 'Готово'
            task.ready_date_time = datetime.datetime.now()
            task.user = request.user  # Сохраняем имя пользователя, который нажал кнопку "Готов"
            task.save()
            return redirect(request.META.get('HTTP_REFERER'))
        except TableTask.DoesNotExist:
            return HttpResponseNotFound("Задача не найдена, возможно уже удалена, вернитесь назад и обновите страницу")
        except Exception as e:
            return HttpResponse(f"Произошла ошибка: {str(e)}")
    else:
        return HttpResponse("Недопустимый запрос")


@login_required
def my_view(request):
    context = {'user': request.user}
    return render(request, 'table_task.html', context)

# def update_stage_view(request, task_id):
#     if request.method == 'POST':
#         try:
#             task = TableTask.objects.get(id=task_id)
#             task.stage = 'Готово'
#             task.ready_date_time = datetime.datetime.now()
#             task.save()
#             return redirect(request.META.get('HTTP_REFERER'))
#         except TableTask.DoesNotExist:
#             return HttpResponseNotFound("Задача не найдена,
#             возможно уже удалена, вернитесь назад и обновите страницу")
#         except Exception as e:
#             return HttpResponse(f"Произошла ошибка: {str(e)}")
#     else:
#         return HttpResponse("Invalid request")
