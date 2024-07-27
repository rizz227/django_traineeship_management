# Generated by Django 5.0.7 on 2024-07-22 18:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0032_remove_project_end_date_remove_project_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffs',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
