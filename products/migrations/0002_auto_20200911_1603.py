# Generated by Django 3.0.5 on 2020-09-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeepod',
            name='pack_size',
            field=models.PositiveIntegerField(choices=[(12, '1 dozen'), (36, '3 dozen'), (60, '5 dozen'), (84, '7 dozen')]),
        ),
    ]