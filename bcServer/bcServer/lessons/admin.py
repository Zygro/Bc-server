from django.contrib import admin

from .models import Lesson, Submit, Comment, Hint
# Register your models here.
admin.site.register(Lesson)
admin.site.register(Submit)
admin.site.register(Comment)
admin.site.register(Hint)
