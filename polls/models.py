from django.db import models
from django.utils import timezone
import datetime
from .jalali_date_conv import shamsiDate
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return '/tag/%s/' % slugify(self.slug)


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250, verbose_name='Title')
    text = models.TextField(verbose_name='Description', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name='Date', blank=True)
    date_created = models.DateTimeField(auto_now_add=timezone.now())
    date_modified = models.DateTimeField(auto_now=timezone.now())
    publish = models.BooleanField(default=True, verbose_name='Publish')
    p_text = models.CharField(max_length=200, default='موافقم', verbose_name='Positive choice text', blank=True, null=True)
    p_votes = models.IntegerField(default=0, verbose_name='Positive choice votes', blank=True, null=True)
    n_text = models.CharField(max_length=200, default='مخالفم', verbose_name='Negative choice text', blank=True, null=True)
    n_votes = models.IntegerField(default=0, verbose_name='Negative choice votes', blank=True, null=True)
    date_limit = models.BooleanField(default=False)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/form-%s/' % self.id

    def jalali_date(self):
        gdate = self.date
        return shamsiDate(gdate.year, gdate.month, gdate.day)

    def p_percent(self):
        sum = self.p_votes + self.n_votes
        if self.p_votes == 0 and self.n_votes == 0:
            percent = 50
        if self.p_votes == 0:
            percent = 0
        else:
            percent = (self.p_votes * 100)/sum
        return percent

    def n_percent(self):
        sum = self.n_votes + self.p_votes
        if self.p_votes == 0 and self.n_votes == 0:
            percent = 50
        if self.n_votes == 0:
            percent = 0
        else:
            percent = (self.n_votes * 100)/sum
        return percent

    def date_limit_checker(self):
        if self.date_limit:
            if timezone.now() < self.start_date < self.end_date:
                return 0
            elif self.start_date < timezone.now() < self.end_date:
                return 1
            elif self.start_date < self.end_date < timezone.now():
                return 2
            else:
                return False
        else:
            return True

    def fa_start_date(self):
        gdate = self.start_date
        return shamsiDate(gdate.year, gdate.month, gdate.day)

    def fa_end_date(self):
        gdate = self.end_date
        return shamsiDate(gdate.year, gdate.month, gdate.day)

    def sum_votes(self):
        return self.p_votes + self.n_votes


class VoteHistory(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=timezone.now(), verbose_name='date')
    user = models.CharField(max_length=150, verbose_name='username')
    ip = models.CharField(max_length=50, verbose_name='voted ip')
    choice = models.CharField(max_length=50, verbose_name='choice')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.user) + ' ' + str(self.ip)


class Comments(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=timezone.now())

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.text

    def jalali_date(self):
        gdate = self.date
        return shamsiDate(gdate.year, gdate.month, gdate.day)
