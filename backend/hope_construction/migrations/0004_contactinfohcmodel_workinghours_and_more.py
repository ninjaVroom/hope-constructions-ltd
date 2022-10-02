# Generated by Django 4.1.1 on 2022-09-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hope_construction', '0003_alter_contactinfohcmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfohcmodel',
            name='workingHours',
            field=models.TextField(blank=True, db_column='ci_hc_working_hours', null=True, verbose_name='Working Hours'),
        ),
        migrations.AlterField(
            model_name='contactinfohcmodel',
            name='instagram',
            field=models.URLField(blank=True, db_column='ci_hc_instagram', null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='contactinfohcmodel',
            name='mondayToFriday',
            field=models.CharField(blank=True, db_column='ci_hc_monday_to_friday', max_length=225, null=True, verbose_name='Monday To Friday Time'),
        ),
        migrations.AlterField(
            model_name='contactinfohcmodel',
            name='saturday',
            field=models.CharField(blank=True, db_column='ci_hc_saturday', max_length=225, null=True, verbose_name='Saturday'),
        ),
        migrations.AlterField(
            model_name='contactinfohcmodel',
            name='sundayAndHolidays',
            field=models.CharField(blank=True, db_column='ci_hc_sunday_and_holidays', max_length=225, null=True, verbose_name='Sundays and Holidays'),
        ),
        migrations.AlterField(
            model_name='contactinfohcmodel',
            name='twitter',
            field=models.URLField(blank=True, db_column='ci_hc_twitter', null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='contactinfohcmodel',
            name='whatsapp',
            field=models.URLField(blank=True, db_column='ci_hc_whatsapp', max_length=225, null=True, verbose_name='Whatsapp'),
        ),
    ]