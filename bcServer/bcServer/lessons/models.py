
import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

# Create your models here.

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('Lesson')
    fun = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    difficulty = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
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

class Submit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('Lesson')
    submittedFile = models.FileField(upload_to='submits')
    result = models.BooleanField(default=False)
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('Lesson')
    text = models.TextField()

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('Lesson')

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

    class Meta:
        unique_together = ('user', 'lesson')
