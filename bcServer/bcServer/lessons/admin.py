from django.contrib import admin

from .models import Lesson, Submit, Comment
# Register your models here.
admin.site.register(Lesson)
admin.site.register(Submit)
admin.site.register(Comment)
