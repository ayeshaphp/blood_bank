# Generated by Django 2.2.3 on 2019-11-03 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20191104_0036'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DonorRegModel',
            new_name='DonorModel',
        ),
    ]