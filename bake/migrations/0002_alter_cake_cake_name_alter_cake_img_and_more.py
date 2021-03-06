# Generated by Django 4.0.1 on 2022-01-13 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='cake_name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='cake',
            name='img',
            field=models.ImageField(upload_to='cakes'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='in_cakes',
            field=models.ManyToManyField(blank=True, to='bake.Cake'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
