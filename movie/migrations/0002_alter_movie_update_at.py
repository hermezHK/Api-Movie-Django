# Generated by Django 4.2.1 on 2023-05-14 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='update_at',
            field=models.DateTimeField(null=True),
        ),
    ]
