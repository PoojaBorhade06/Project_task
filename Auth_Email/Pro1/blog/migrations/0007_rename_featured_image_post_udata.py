# Generated by Django 3.2.7 on 2021-09-16 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='featured_image',
            new_name='udata',
        ),
    ]
