from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Question)
admin.site.register(models.Comments)
admin.site.register(models.Tag)
admin.site.register(models.VoteHistory)
