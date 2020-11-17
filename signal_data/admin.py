from django.contrib import admin
from .models import DataSignal


@admin.register(DataSignal)
class DataSignalAdmin(admin.ModelAdmin):
    list_display = [
        'uuid',
        'signal_type',
        'signal_value',
        'valid',
        'added',
    ]
    list_filter = [
        'signal_type',
        'valid',
    ]
    readonly_fields = [
        'added',
        'signal_meta',
    ]
