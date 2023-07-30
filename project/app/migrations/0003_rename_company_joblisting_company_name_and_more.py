# Generated by Django 4.2.3 on 2023-07-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_joblisting_delete_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joblisting',
            old_name='company',
            new_name='company_name',
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='job_type',
            field=models.CharField(choices=[('onsite', 'On-site'), ('remote', 'Remote'), ('internship', 'Internship'), ('fulltime', 'Full-time')], max_length=20),
        ),
    ]
