# Generated by Django 4.2 on 2023-09-22 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_student_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/'),
        ),
    ]
