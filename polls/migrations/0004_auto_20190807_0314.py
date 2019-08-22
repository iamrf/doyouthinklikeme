# Generated by Django 2.2.4 on 2019-08-07 03:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_date_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='n_text',
            field=models.CharField(blank=True, default='مخالفم', max_length=200, null=True, verbose_name='Negative choice text'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='n_votes',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Negative choice votes'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='p_text',
            field=models.CharField(blank=True, default='موافقم', max_length=200, null=True, verbose_name='Positive choice text'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='p_votes',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Positive choice votes'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]