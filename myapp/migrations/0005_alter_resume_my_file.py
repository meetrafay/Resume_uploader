# Generated by Django 3.2.8 on 2022-04-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_resume_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='my_file',
            field=models.FileField(blank=True, upload_to='myapp/doc'),
        ),
    ]
