# Generated by Django 2.2.4 on 2019-08-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190806_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='date_limit',
            field=models.BooleanField(default=False),
        ),
    ]