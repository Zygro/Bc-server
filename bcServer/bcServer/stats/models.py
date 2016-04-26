from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.apps import apps
from django.db.models import Avg
from bcServer.lessons.models import Submit
from django.db.models.signals import pre_save
# Create your models here.

class Rating(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('lessons.Lesson')

    difficulty = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    fun = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    def __str__ (self):
        return (self.user.username+"-"+self.lesson.name)
    class Meta:
        unique_together=('user','lesson')

class LessonStat(models.Model):
    lesson = models.OneToOneField('lessons.Lesson')
    avg_fun = models.FloatField(null=True, blank=True)
    avg_diff = models.FloatField(null=True, blank=True)
    good_solutions = models.IntegerField(null=True, blank=True)
    bad_solutions = models.IntegerField(null=True, blank=True)
    def __str__ (self):
        return self.lesson.name


class UserStat(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    progress = models.IntegerField(default=1)
    def __str__ (self):
        return self.user.username

class User_LessonStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('lessons.Lesson')
    def __str__ (self):
        return (self.user.username+"-"+self.lesson.name)
    class Meta:
        unique_together=('lesson','user')


def set_avg_fun (sender, instance, *args, **kwargs):
    avg = Rating.objects.filter(lesson=instance.lesson).aggregate(Avg('fun'))['fun__avg']
    instance.avg_fun = avg
def set_avg_diff (sender, instance, *args, **kwargs):
    avg = Rating.objects.filter(lesson=instance.lesson).aggregate(Avg('difficulty'))['difficulty__avg']
    instance.avg_diff = avg
def set_good_solutions (sender, instance, *args, **kwargs):
    Submit = apps.get_model('lessons','submit')
    good_submits = Submit.objects.filter(lesson=instance.lesson, result=True)
    instance.good_solutions = len(good_submits)
def set_bad_solutions (sender, instance, *args, **kwargs):
    Submit = apps.get_model('lessons','submit')
    bad_submits = Submit.objects.filter(lesson=instance.lesson, result=False)
    instance.bad_solutions = len(bad_submits)

pre_save.connect(set_good_solutions, sender=LessonStat)
pre_save.connect(set_bad_solutions, sender=LessonStat)
pre_save.connect(set_avg_fun, sender=LessonStat)
pre_save.connect(set_avg_diff, sender=LessonStat)
