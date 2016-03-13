from django.contrib import admin

from .models import Lesson, Submit, Rating, Comment
# Register your models here.
admin.site.register(Lesson)
admin.site.register(Submit)
admin.site.register(Rating)
admin.site.register(Comment)
