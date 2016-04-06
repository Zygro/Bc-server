from django.conf.urls import url, patterns

from .views import LessonViewSet, SubmitViewSet, CommentViewSet, HintViewSet

urlpatterns = [
    url(r'^$', LessonViewSet.as_view({'get':'show'})),
    url(r'^(?P<lessonID>[0-9]+)/submits/$', SubmitViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^api/(?P<lessonID>[0-9]+)/submitfile/$', SubmitViewSet.as_view({'get':'list', 'post': 'create'})),
    url(r'^api/(?P<lessonID>[0-9]+)/discussion/$', CommentViewSet.as_view({'get':'list', 'post':'create'})),
    url(r'^api/(?P<lessonID>[0-9]+)/hints/$', HintViewSet.as_view({'get':'list'})),
    url(r'^api/(?P<lessonID>[0-9]+)/newhint/$', HintViewSet.as_view({'get':'get_new_hint'})),
    url(r'^api/lessonslist/$', LessonViewSet.as_view({'get': 'list'})),
    url(r'^(?P<lessonID>[0-9]+)/$', LessonViewSet.as_view({'get':'showSingleLesson'})),
]
