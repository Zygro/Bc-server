from django.db import models

class LessonStat(models.Model):
    lesson = models.ForeignKey('lessons.Lesson')
    def __str__ (self):
        return self.lesson.name

# Create your models here.
