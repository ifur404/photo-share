# Generated by Django 3.1.6 on 2021-02-18 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photos',
            new_name='Photo',
        ),
    ]