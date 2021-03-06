# Generated by Django 4.0.1 on 2022-01-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_name', models.CharField(max_length=20)),
                ('img', models.FilePathField(default='C:\\Users\\Artem\\Desktop\\Proggers\\GitHub\\Cake_Time\\assets/cakes/')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=20)),
                ('in_cakes', models.ManyToManyField(to='bake.Cake')),
            ],
        ),
        migrations.AddField(
            model_name='cake',
            name='composition',
            field=models.ManyToManyField(to='bake.Ingredient'),
        ),
    ]
