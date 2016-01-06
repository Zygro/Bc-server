
import datetime
from django.db import models
from django.utils import timezone

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
