from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('table-task/', views.table_task_view, name='table_task'),
    path('table-task/unready/', views.unready_table_view, name='unready_task'),
    path('table-task/ready/', views.ready_table_view, name='ready_task'),
    path('update-stage/<int:task_id>/', views.update_stage_view, name='update_stage'),
]
