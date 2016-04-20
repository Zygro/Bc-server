from django.conf.urls import url, patterns

from .views import LessonViewSet, SubmitViewSet, CommentViewSet, HintViewSet, SingleLessonView

urlpatterns = [
    url(r'^lessons/$', LessonViewSet.as_view({'get':'show'}),name='lessonsList'),
    url(r'^lessons/(?P<lessonID>[0-9]+)/$', SingleLessonView.as_view()),
    url(r'^api/submits/(?P<lessonID>[0-9]+)/$', SubmitViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^api/(?P<lessonID>[0-9]+)/submitfile/$', SubmitViewSet.as_view({'get':'list', 'post': 'create'})),
    url(r'^api/discussion/(?P<lessonID>[0-9]+)/$', CommentViewSet.as_view({'get':'list', 'post':'create'})),
    url(r'^api/hints/(?P<lessonID>[0-9]+)/$', HintViewSet.as_view({'get':'list'})),
    url(r'^api/newhint/(?P<lessonID>[0-9]+)/$', HintViewSet.as_view({'get':'get_new_hint'})),
    url(r'^api/lessonslist/$', LessonViewSet.as_view({'get': 'list'})),
    url(r'^api/lesson/(?P<lessonID>[0-9]+)/$', LessonViewSet.as_view({'get':'singleLesson'}))
]
