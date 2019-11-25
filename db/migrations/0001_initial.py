# Generated by Django 2.2.7 on 2019-11-25 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Director')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('release', models.DateField(verbose_name='Estreno')),
                ('runtime', models.IntegerField(verbose_name='Duración')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('poster', models.CharField(max_length=150, verbose_name='Poster')),
                ('imdbRating', models.CharField(max_length=6, verbose_name='IMDB')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Director')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('price', models.IntegerField(verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='PlatformContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Movie')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Platform')),
            ],
        ),
    ]
