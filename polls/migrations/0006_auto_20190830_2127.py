# Generated by Django 2.2.4 on 2019-08-30 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190830_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='slg',
            new_name='slug',
        ),
    ]