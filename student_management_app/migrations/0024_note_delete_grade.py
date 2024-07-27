# Generated by Django 5.0.7 on 2024-07-20 23:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0023_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.courses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='student_management_app.students')),
            ],
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
