from . import views
from django.conf.urls import url


urlpatterns = [
    url(
        r'^$',
        views.index,
        name='index'
    ),
    url(
        r'^events/$',
        views.EventListView.as_view(),
        name='events',
    ),
    url(
        r'^event/(?P<pk>\d+)$',
        views.EventDetailView.as_view(),
        name='event-detail',
    ),
]
