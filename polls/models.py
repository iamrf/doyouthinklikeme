from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    text = models.TextField(verbose_name='Description', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name='Date')
    date_created = models.DateTimeField(auto_now_add=timezone.now())
    date_modified = models.DateTimeField(auto_now=timezone.now())
    publish = models.BooleanField(default=True, verbose_name='Publish')

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    p_text = models.CharField(max_length=200, default='+', verbose_name='Positive choice text')
    p_votes = models.IntegerField(default=0, verbose_name='Positive choice votes')
    n_text = models.CharField(max_length=200, default='-', verbose_name='Negative choice text')
    n_votes = models.IntegerField(default=0, verbose_name='Negative choice votes')

    def __str__(self):
        return self.text
