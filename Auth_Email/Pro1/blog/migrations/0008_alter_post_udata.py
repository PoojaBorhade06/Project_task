# Generated by Django 3.2.7 on 2021-09-17 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_featured_image_post_udata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='udata',
            field=models.FileField(upload_to='media/'),
        ),
    ]
