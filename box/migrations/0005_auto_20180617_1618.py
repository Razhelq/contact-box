# Generated by Django 2.0.5 on 2018-06-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0004_auto_20180617_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.FileField(null=True, upload_to='', verbose_name='Photo'),
        ),
    ]
