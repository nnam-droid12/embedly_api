# Generated by Django 3.1.3 on 2021-02-07 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210208_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedembed',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]