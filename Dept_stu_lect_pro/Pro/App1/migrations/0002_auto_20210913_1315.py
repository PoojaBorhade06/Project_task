# Generated by Django 3.2.7 on 2021-09-13 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecturer',
            old_name='Department',
            new_name='Dept_lec',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Department',
            new_name='Dept_stu',
        ),
    ]
