from django.conf.urls import url, patterns

from .views import LessonViewSet, SubmitViewSet

urlpatterns = [
    url(r'^$', LessonViewSet.as_view({'get': 'list'})),
    url(r'^(?P<lessonID>[0-9]+)/submits/$', SubmitViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^(?P<lessonID>[0-9]+)/submitfile/$', SubmitViewSet.as_view({'get':'list', 'post': 'create'}))
]
