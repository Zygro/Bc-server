from django.conf.urls import url

from .views import UserViewSet

urlpatterns = [
    url(r'^$', UserViewSet.as_view({'get': 'list'})),
    url(r'^login', UserViewSet.as_view({'post': 'login'})),
]
