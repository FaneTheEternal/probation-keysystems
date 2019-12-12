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
    url(
        r'^user/$',
        views.UserDetailView,
        name='user-detail',
    ),
    url(
        r'^user/events/$',
        views.UserEventsListView.as_view(),
        name='user-events',
    ),
    url(
        r'event/(?P<pk>\d+)/partic/',
        views.ParticipateView,
        name='i-do-event',
    ),
    url(
        r'^event/(?P<pk>\d+)/delete-partic/$',
        views.ParticipateDeleteView,
        name='i-remind-event',
    ),
]
