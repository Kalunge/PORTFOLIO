# Generated by Django 3.0 on 2019-12-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20191206_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/img'),
        ),
    ]