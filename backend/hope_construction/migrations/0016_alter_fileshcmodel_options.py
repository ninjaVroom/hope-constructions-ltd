# Generated by Django 4.1.1 on 2022-09-30 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hope_construction', '0015_alter_fileshcmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fileshcmodel',
            options={'managed': True, 'verbose_name': 'File', 'verbose_name_plural': 'Files'},
        ),
    ]
