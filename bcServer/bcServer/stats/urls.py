from django.conf.urls import url, patterns

from .views import RatingViewSet

urlpatterns = [
    url(r'^(?P<lessonID>[0-9]+)/rating/$', RatingViewSet.as_view({'get': 'list', 'post': 'create'})),
]
