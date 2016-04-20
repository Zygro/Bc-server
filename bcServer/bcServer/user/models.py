from django.db import models
from django.conf import settings
# Create your models here.

class UserLessonWrapper(models.Model):
    lesson = models.ForeignKey('lessons.Lesson')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    completed = models.BooleanField(default = False)
    hints_used = models.IntegerField(default = 0)
    def __str__ (self):
        return self.lesson.name + ' ' + self.user.username
    class Meta:
        unique_together=('user','lesson')
