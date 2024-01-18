from django.contrib import admin
from logs.models import Log

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'channel', 'token', 'user_id', 'is_error_occurred', 'error', 'n_generated_token', 'n_context_token', 'model', 'cost', 'complete_time', 'created_at')
    list_filter = ('channel', 'is_error_occurred', 'model')
    search_fields = ('question', 'answer', 'channel', 'token', 'user_id', 'error', 'n_generated_token', 'n_context_token', 'model', 'cost', 'complete_time')
    ordering = ('-created_at',)
