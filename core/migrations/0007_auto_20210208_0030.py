# Generated by Django 3.1.3 on 2021-02-07 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210208_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedembed',
            name='version',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
