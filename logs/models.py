from django.db import models

class Log(models.Model):
    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    channel = models.CharField(max_length=1000, null=True, blank=True)
    token = models.CharField(max_length=1000, null=True, blank=True)
    user_id = models.CharField(max_length=1000, null=True, blank=True)
    is_error_occurred = models.BooleanField(default=False)
    error = models.TextField(null=True, blank=True)
    n_generated_token = models.CharField(max_length=1000, null=True, blank=True)
    n_context_token = models.CharField(max_length=1000, null=True, blank=True)
    model = models.CharField(max_length=1000, null=True, blank=True)
    cost = models.CharField(max_length=1000, null=True, blank=True)
    complete_time = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Logs'
        ordering = ('-created_at',)
