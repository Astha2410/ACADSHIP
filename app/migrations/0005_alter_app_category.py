# Generated by Django 4.0 on 2022-03-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_app_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='category',
            field=models.CharField(blank=True, choices=[('None', 'NONE'), ('National', 'NATIONAL'), ('International', 'INTERNATIONAL')], max_length=200, null=True, verbose_name='Category'),
        ),
    ]