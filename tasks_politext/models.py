from django.contrib.auth.models import User
from django.db import models


class TableTask(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(null=True, max_length=150, verbose_name="Название")
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="Время файла")
    add_date_time = models.DateTimeField(blank=True, null=True, verbose_name="Время добавления")
    equipment = models.CharField(max_length=100, blank=True, null=True, verbose_name="Оборудование")
    stage = models.CharField(max_length=100, null=True, default='На выводе', verbose_name="Состояние")
    ready_date_time = models.DateTimeField(blank=True, null=True, verbose_name="Время готовности")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True,
        default="---"
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

