from django.conf.urls import url

from .views import LessonViewSet

urlpatterns = [
    url(r'^$', LessonViewSet.as_view({'get': 'list'})),
]
