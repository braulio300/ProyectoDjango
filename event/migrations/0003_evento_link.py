# Generated by Django 3.1.3 on 2020-11-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20201111_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
