# Generated by Django 2.1.4 on 2018-12-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitionsummary', '0006_auto_20181213_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='start',
            field=models.DateField(null=True, verbose_name='Start date'),
        ),
    ]