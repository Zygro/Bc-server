
import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=256)
    problem = models.TextField()
    pub_date = models.DateTimeField('date published')
    good_solutions = models.IntegerField(default=0)
    bad_solutions = models.IntegerField(default=0)
    number = models.IntegerField(default=1)
    optional = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Submit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('Lesson')
    submittedFile = models.FileField(upload_to='submits')

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
