# Generated by Django 3.1.3 on 2020-11-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['-created'], 'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterField(
            model_name='evento',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creación'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='image',
            field=models.ImageField(upload_to='Imagen Eventos', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualización'),
        ),
    ]