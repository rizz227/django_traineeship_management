# Generated by Django 5.0.7 on 2024-07-15 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0012_students_preferred_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='preferred_category',
            field=models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening')], max_length=10),
        ),
    ]
