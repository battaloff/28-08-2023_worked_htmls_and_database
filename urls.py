from django.urls import path
from .views import table_task_view, update_stage_view, unready_table_view, ready_table_view

urlpatterns = [
    path('table-task/', table_task_view, name='table_task'),
    path('table-task/unready/', unready_table_view, name='unready_task'),
    path('table-task/ready/', ready_table_view, name='ready_task'),
    path('update-stage/<int:task_id>/', update_stage_view, name='update_stage'),
    # Другие URL-пути вашего приложения
]

