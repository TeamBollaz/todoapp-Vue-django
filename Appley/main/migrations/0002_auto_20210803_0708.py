# Generated by Django 3.2.4 on 2021-08-03 04:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='region',
            field=models.CharField(max_length=100, null=True, verbose_name='Where Found'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='fruitname',
            field=models.CharField(max_length=100, verbose_name='Fruitname'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='ftype',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Fruit Type'),
            preserve_default=False,
        ),
    ]
