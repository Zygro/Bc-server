from django.db import models
from django.conf import settings
# Create your models here.

class UserLessonWrapper(models.Model):
    lesson = models.ForeignKey('lessons.Lesson')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    completed = models.BooleanField(default = False)
    def __str__ (self):
        return self.lesson.name + ' ' + self.user.email
