# Generated by Django 3.0.8 on 2020-07-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_auto_20200725_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='Phone_no',
            field=models.IntegerField(default=910123456789),
        ),
        migrations.AlterField(
            model_name='host',
            name='flat_no',
            field=models.IntegerField(default=0),
        ),
    ]
