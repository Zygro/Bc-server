from django.conf.urls import url

from .views import UserViewSet, WrapperViewSet

urlpatterns = [
    url(r'^profile',UserViewSet.as_view({'get':'displayProfile'})),
    url(r'^api/profile', UserViewSet.as_view({'get': 'profile'})),
    url(r'^login', UserViewSet.as_view({'get':'loginView','post': 'login'})),
    url(r'^logout', UserViewSet.as_view({'get':'logout'})),
    url(r'^register', UserViewSet.as_view({'post': 'create'})),
    url(r'^update', UserViewSet.as_view({'post': 'update_profile'})),
    url(r'^api/(?P<lessonID>[0-9]+)/wrapper/$', WrapperViewSet.as_view({'get':'list'})),
]
