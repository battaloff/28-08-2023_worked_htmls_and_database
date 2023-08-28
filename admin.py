from django.contrib import admin
from .models import TableTask


class TableTaskAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "file_name",
                    "add_date_time",
                    "equipment",
                    "stage",
                    "ready_date_time"
                    ]

    list_filter = ['stage', 'add_date_time', 'ready_date_time', 'equipment']
    search_fields = ['file_name']
    readonly_fields = ['id', 'add_date_time']


admin.site.register(TableTask, TableTaskAdmin)
