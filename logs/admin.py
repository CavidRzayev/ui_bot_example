from django.contrib import admin
from logs.models import Log

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'channel', 'token', 'user_id', 'is_error_occurred', 'error', 'num_of_input_tokens', 'num_of_output_tokens', 'model', 'cost', 'requested_at', 'multiquery_started_at', 'multiquery_ended_at', 'llm_request_started_at', 'llm_request_ended_at', 'llm_response_started_at', 'llm_response_ended_at', 'created_at')
    list_filter = ('channel', 'is_error_occurred', 'model')
    search_fields = ('question', 'answer', 'channel', 'token', 'user_id', 'error', 'num_of_input_tokens', 'model', 'cost')
    ordering = ('-created_at',)
