# Generated by Django 2.2.7 on 2019-11-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='image',
            field=models.CharField(max_length=50, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
