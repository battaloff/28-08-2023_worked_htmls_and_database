# Generated by Django 4.2.4 on 2023-08-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_politext', '0006_alter_tabletask_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabletask',
            name='change_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время файла'),
        ),
    ]