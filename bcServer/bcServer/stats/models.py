from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
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

class LessonStat(models.Model):
    lesson = models.ForeignKey('lessons.Lesson')
    avg_fun = models.FloatField(null=True, blank=True)
    avg_diff = models.FloatField(null=True, blank=True)
    def __str__ (self):
        return self.lesson.name

def set_avg_fun (sender, instance, *args, **kwargs):
    avg = Rating.objects.filter(lesson=instance.lesson).aggregate(Avg('fun'))['fun__avg']
    instance.avg_fun = avg
def set_avg_diff (sender, instance, *args, **kwargs):
    avg = Rating.objects.filter(lesson=instance.lesson).aggregate(Avg('difficulty'))['difficulty__avg']
    instance.avg_diff = avg

pre_save.connect(set_avg_fun, sender=LessonStat)
pre_save.connect(set_avg_diff, sender=LessonStat)
class UserStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __str__ (self):
        return self.user.email
class User_LessonStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('lessons.Lesson')
    def __str__ (self):
        return (self.user.email+"-"+self.lesson.name)
