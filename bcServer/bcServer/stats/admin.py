from django.contrib import admin

# Register your models here.
from .models import LessonStat, UserStat
admin.site.register(LessonStat)
admin.site.register(UserStat)
