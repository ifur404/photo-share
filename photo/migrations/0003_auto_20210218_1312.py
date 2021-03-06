# Generated by Django 3.1.6 on 2021-02-18 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20210218_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='images',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photo.category'),
        ),
    ]
