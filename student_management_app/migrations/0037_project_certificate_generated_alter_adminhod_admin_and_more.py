# Generated by Django 5.0.7 on 2024-07-23 10:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0036_alter_staffs_admin_alter_students_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='certificate_generated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='adminhod',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='adminhod', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='students',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
