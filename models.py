from django.db import models


class TableTask(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=150, verbose_name="Название")
    add_date_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name="Время добавления")
    equipment = models.CharField(max_length=100, blank=True, verbose_name="Оборудование")
    stage = models.CharField(max_length=100,  default='На выводе', verbose_name="Состояние")
    ready_date_time = models.DateTimeField(blank=True, null=True, verbose_name="Время готовности")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

