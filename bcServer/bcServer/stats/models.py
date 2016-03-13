from django.db import models
from django.conf import settings

# Create your models here.

class LessonStat(models.Model):
    lesson = models.ForeignKey('lessons.Lesson')
    def __str__ (self):
        return self.lesson.name
class UserStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __str__ (self):
        return self.user.email
