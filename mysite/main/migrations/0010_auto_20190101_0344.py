# Generated by Django 2.1.4 on 2019-01-01 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190101_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burd326',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]
