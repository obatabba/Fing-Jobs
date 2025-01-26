# Generated by Django 5.1.5 on 2025-01-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0005_application_employee_applied_jobs'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='application',
            constraint=models.UniqueConstraint(fields=('applicant', 'job'), name='unique-application'),
        ),
    ]
