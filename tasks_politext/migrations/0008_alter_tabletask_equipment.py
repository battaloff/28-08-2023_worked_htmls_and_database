# Generated by Django 4.2.4 on 2023-08-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_politext', '0007_tabletask_change_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabletask',
            name='equipment',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Оборудование'),
        ),
    ]