# Generated by Django 5.0.7 on 2024-07-24 08:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0037_project_certificate_generated_alter_adminhod_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificat',
            name='course_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
