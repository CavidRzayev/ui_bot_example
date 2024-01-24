from django.db import models

class Log(models.Model):
    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    channel = models.CharField(max_length=1000, null=True, blank=True)
    token = models.CharField(max_length=1000, null=True, blank=True)
    user_id = models.CharField(max_length=1000, null=True, blank=True)
    is_error_occurred = models.BooleanField(default=False)
    error = models.TextField(null=True, blank=True)
    num_of_input_tokens = models.IntegerField(null=True, blank=True)
    num_of_output_tokens = models.IntegerField(null=True, blank=True)
    model = models.CharField(max_length=1000, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    requested_at = models.DateTimeField(null=True, blank=True)
    multiquery_started_at = models.DateTimeField(null=True, blank=True)
    multiquery_ended_at = models.DateTimeField(null=True, blank=True)
    llm_request_started_at = models.DateTimeField(null=True, blank=True)
    llm_request_ended_at = models.DateTimeField(null=True, blank=True)
    llm_response_started_at = models.DateTimeField(null=True, blank=True)
    llm_response_ended_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Logs'
        ordering = ('-created_at',)
