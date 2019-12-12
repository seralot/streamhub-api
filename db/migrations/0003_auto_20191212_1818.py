# Generated by Django 3.0 on 2019-12-12 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20191203_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('photo', models.CharField(max_length=150, verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'actor',
                'verbose_name_plural': 'Actores',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.RemoveField(
            model_name='platform',
            name='content4k',
        ),
        migrations.RemoveField(
            model_name='platformcontent',
            name='num_episodes',
        ),
        migrations.AddField(
            model_name='content',
            name='trailer',
            field=models.CharField(default='trailer', max_length=150, verbose_name='Trailer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='devicesBasic',
            field=models.IntegerField(default=5, verbose_name='Dispositivos Basico'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='devicesPremium',
            field=models.IntegerField(default=5, verbose_name='Dispositivos Premium'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='devicesStandard',
            field=models.IntegerField(default=5, verbose_name='Dispositivos Estandár'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='noConnection',
            field=models.BooleanField(default=1, verbose_name='Sin Conexión'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='parentalControl',
            field=models.BooleanField(default=1, verbose_name='Control Parental'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='profiles',
            field=models.IntegerField(default=5, verbose_name='Perfiles'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='resolutionBasic',
            field=models.CharField(default='SD', max_length=20, verbose_name='Resolución Basico'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='resolutionPremium',
            field=models.CharField(default='4K', max_length=20, verbose_name='Resolución Premium'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='resolutionStandard',
            field=models.CharField(default='HD', max_length=20, verbose_name='Resolución Estandár'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='content',
            name='director',
        ),
        migrations.AddField(
            model_name='content',
            name='director',
            field=models.ManyToManyField(to='db.Director'),
        ),
        migrations.RemoveField(
            model_name='content',
            name='genre',
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='priceBasic',
            field=models.IntegerField(verbose_name='Precio Basico'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='pricePremium',
            field=models.IntegerField(verbose_name='Precio Premium'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='priceStandard',
            field=models.IntegerField(verbose_name='Precio Estandár'),
        ),
        migrations.CreateModel(
            name='ActorContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(verbose_name='Principal')),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Actor')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Content')),
            ],
            options={
                'verbose_name': 'actor contenido',
                'verbose_name_plural': 'Actores Contenido',
            },
        ),
        migrations.AddField(
            model_name='content',
            name='genre',
            field=models.ManyToManyField(to='db.Genre'),
        ),
    ]
