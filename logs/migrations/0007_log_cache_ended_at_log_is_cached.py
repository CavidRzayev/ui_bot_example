# Generated by Django 4.2.9 on 2024-01-31 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0006_alter_log_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='cache_ended_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='is_cached',
            field=models.BooleanField(default=False),
        ),
    ]