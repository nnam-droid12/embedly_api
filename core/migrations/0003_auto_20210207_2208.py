# Generated by Django 3.1.3 on 2021-02-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210207_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedembed',
            name='author_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]