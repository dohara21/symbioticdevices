# Generated by Django 2.1.4 on 2018-12-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitionsummary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='summary',
            options={'verbose_name': 'Exhibition Summary', 'verbose_name_plural': 'Exhibition Summaries'},
        ),
        migrations.AddField(
            model_name='summary',
            name='address',
            field=models.CharField(default='Some String', max_length=300, verbose_name='Delivery address'),
        ),
        migrations.AddField(
            model_name='summary',
            name='banners',
            field=models.TextField(default='Some String', max_length=200, verbose_name='Banners'),
        ),
        migrations.AddField(
            model_name='summary',
            name='brochures',
            field=models.TextField(default='Some String', help_text='Include qty', max_length=500, verbose_name='Brochures'),
        ),
        migrations.AddField(
            model_name='summary',
            name='delivery',
            field=models.BooleanField(default=False, null=True, verbose_name='Delivered'),
        ),
        migrations.AddField(
            model_name='summary',
            name='details',
            field=models.TextField(default='Some String', help_text='Artwork required, important links etc.', max_length=400, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='summary',
            name='equipment',
            field=models.TextField(default='Some String', max_length=500, verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='summary',
            name='hand',
            field=models.BooleanField(default=False, null=True, verbose_name='Hand carried'),
        ),
        migrations.AddField(
            model_name='summary',
            name='power',
            field=models.BooleanField(default=False, null=True, verbose_name='Power supplied'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='accommodation',
            field=models.CharField(max_length=300, verbose_name='Accomodation address'),
        ),
    ]