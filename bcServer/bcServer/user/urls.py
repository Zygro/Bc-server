from django.conf.urls import url

from .views import UserViewSet

urlpatterns = [
    url(r'^$', UserViewSet.as_view({'get': 'profile'})),
    url(r'^login', UserViewSet.as_view({'get':'loginView','post': 'login'})),
    url(r'^register', UserViewSet.as_view({'post': 'create'})),
    url(r'^update', UserViewSet.as_view({'post': 'update_profile'})),
]
