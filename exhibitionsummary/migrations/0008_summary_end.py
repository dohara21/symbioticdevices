# Generated by Django 2.1.4 on 2018-12-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitionsummary', '0007_summary_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='end',
            field=models.DateField(null=True, verbose_name='End date'),
        ),
    ]
