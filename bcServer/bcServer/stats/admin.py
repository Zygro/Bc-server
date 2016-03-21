from django.contrib import admin

# Register your models here.
from .models import LessonStat, UserStat, Rating
admin.site.register(LessonStat)
admin.site.register(UserStat)
admin.site.register(Rating)
