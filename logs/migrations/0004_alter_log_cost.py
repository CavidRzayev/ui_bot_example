# Generated by Django 4.2.9 on 2024-01-29 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_remove_log_complete_time_remove_log_n_context_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
    ]
