# Generated by Django 3.0.5 on 2020-05-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Hamburguesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField(max_length=1000)),
                ('img', models.URLField()),
                ('ingredientes', models.ManyToManyField(to='anvorguesa.Ingrediente')),
            ],
        ),
    ]
