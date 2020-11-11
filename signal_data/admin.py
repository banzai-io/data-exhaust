from django.contrib import admin
from .models import DataSignal


@admin.register(DataSignal)
class DataSignalAdmin(admin.ModelAdmin):
    list_display = []