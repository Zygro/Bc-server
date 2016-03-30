from django.conf.urls import url, patterns

from .views import RatingViewSet, DueToChangeViewSet

urlpatterns = [
    url(r'^(?P<lessonID>[0-9]+)/rating/$', RatingViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'duetochange/', DueToChangeViewSet.as_view({'get':'list'}))
]
