# Generated by Django 3.1.3 on 2021-02-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210208_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedembed',
            name='thumbnail_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='savedembed',
            name='thumbnail_width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
