# Generated by Django 5.0.7 on 2024-07-27 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0004_certificat_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificat',
            name='course_date',
        ),
        migrations.RemoveField(
            model_name='certificat',
            name='course_name',
        ),
        migrations.RemoveField(
            model_name='certificat',
            name='director_signature',
        ),
        migrations.RemoveField(
            model_name='certificat',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='certificat',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='certificat',
            name='staff_name',
        ),
    ]
