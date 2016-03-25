
import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from django.db.models.signals import post_save
from bcServer.stats.models import LessonStat
# Create your models here.


class Lesson(models.Model):
    name = models.CharField(max_length=256)
    problem = models.TextField()
    pub_date = models.DateTimeField('date published')
    good_solutions = models.IntegerField(default=0)
    bad_solutions = models.IntegerField(default=0)
    number = models.IntegerField(default=1)
    optional = models.BooleanField(default=True)
    inputs = models.FileField(null=True, blank=True)
    correct_solution = models.FileField(null=True, blank=True)
    #fun = models.IntegerField(default=Rating.objects.filter(lesson=id).aggregate(Avg('fun')))

    def __str__(self):
        return self.name

def MakeNewLesson (sender, instance, *args, **kwargs):
    stat = LessonStat(lesson=instance)
    print(stat)
    stat.save()
post_save.connect(MakeNewLesson, sender=Lesson)

class Submit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('Lesson')
    submittedFile = models.FileField(upload_to='submits')
    result = models.BooleanField(default=False)
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('Lesson')
    text = models.TextField()
