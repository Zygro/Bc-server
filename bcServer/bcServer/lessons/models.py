
import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from django.db.models.signals import post_save, pre_save
from django.apps import apps
from django.db.models import F
# Create your models here.


class Lesson(models.Model):
    name = models.CharField(max_length=256)
    problem = models.TextField()
    pub_date = models.DateTimeField('date published')
    number = models.IntegerField(default=1)
    optional = models.BooleanField(default=True)
    inputs = models.FileField(null=True, blank=True,upload_to='inputs')
    correct_solution = models.FileField(null=True, blank=True, upload_to='outputs')

    def __str__(self):
        return self.name

def PushOtherLessons (sender, instance, *args, **kwargs):
    if not(instance.optional):
        rank = instance.number
        non_optionals = [x for x in Lesson.objects.all().order_by('number') if not(x.optional) and x.id!=instance.id]
        for l in non_optionals:
            while len(Lesson.objects.filter(number = (l.number-1)))==0 and l.number>1:
                Lesson.objects.filter(id=l.id).update(number = F('number')-1)
                l.number -= 1
        if len(Lesson.objects.filter(number=rank))>0:
            Lesson.objects.filter(number__gte = rank, optional=False).exclude(id=instance.id).update(number = F('number')+1)
        non_optionals = [x for x in Lesson.objects.all().order_by('number') if not(x.optional) and x.id!=instance.id]
        for l in non_optionals:
            while len(Lesson.objects.filter(number = (l.number-1)))==0 and l.number>1:
                Lesson.objects.filter(id=l.id).update(number = F('number')-1)
                l.number -= 1

        while len(Lesson.objects.filter(number = (instance.number-1)))==0 and instance.number>1:
            Lesson.objects.filter(id=instance.id).update(number = F('number')-1)
            instance.number -= 1
def MakeLessonStat (sender, instance, *args, **kwargs):
    if len(apps.get_model('stats', 'LessonStat').objects.filter(lesson_id=instance.id))==0 :
        stat = apps.get_model('stats', 'LessonStat')(lesson=instance)
        stat.save()
post_save.connect(MakeLessonStat, sender=Lesson)
post_save.connect(PushOtherLessons, sender=Lesson)

class Submit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('Lesson')
    submittedFile = models.FileField(upload_to='submits')
    result = models.BooleanField(default=False)
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lesson = models.ForeignKey('Lesson')
    text = models.TextField()
