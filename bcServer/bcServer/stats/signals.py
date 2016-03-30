
from django.apps import apps
from django.db.models import Avg
from django.db.models.signals import pre_save

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

pre_save.connect(set_good_solutions, sender=apps.get_model('stats','LessonStat'))
pre_save.connect(set_bad_solutions, sender=apps.get_model('stats','LessonStat'))
pre_save.connect(set_avg_fun, sender=apps.get_model('stats','LessonStat'))
pre_save.connect(set_avg_diff, sender=apps.get_model('stats','LessonStat'))
