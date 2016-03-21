from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

# Create your models here.

class LessonStat(models.Model):
    lesson = models.ForeignKey('lessons.Lesson')
    def __str__ (self):
        return self.lesson.name
class UserStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __str__ (self):
        return self.user.email
class User_LessonStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('lessons.Lesson')
    def __str__ (self):
        return (self.user.email+"-"+self.lesson.name)

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
