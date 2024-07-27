# Generated by Django 5.0.7 on 2024-07-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0039_alter_project_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='course',
        ),
        migrations.AddField(
            model_name='group',
            name='courses',
            field=models.ManyToManyField(related_name='groups', to='student_management_app.courses'),
        ),
    ]
