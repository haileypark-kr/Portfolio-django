# Generated by Django 2.0.2 on 2019-01-31 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='examples',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='pdf_file',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
    ]
