# Generated by Django 2.2.7 on 2019-11-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('release', models.DateField(verbose_name='Release')),
                ('runtime', models.IntegerField(verbose_name='Time')),
                ('director', models.CharField(max_length=30, verbose_name='Director')),
                ('description', models.TextField(verbose_name='Description')),
                ('poster', models.CharField(max_length=150, verbose_name='Poster')),
                ('imdbRating', models.CharField(max_length=6, verbose_name='IMDB')),
                ('platform', models.CharField(max_length=100, verbose_name='Streaming')),
            ],
        ),
    ]
