# Generated by Django 4.2.7 on 2023-12-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verify',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
