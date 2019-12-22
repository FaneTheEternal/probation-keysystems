from . import views
from django.conf.urls import url


urlpatterns = [
    url(
        r'^$',
        views.index,
        name='index'
    ),
    url(
        r'^account/$',
        views.UserDetailView,
        name='user-detail',
    ),
    url(
        r'^account/events/$',
        views.UserEventsListView.as_view(),
        name='user-events',
    ),
]

# Event list & details
urlpatterns += [
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

# Event create & upd & del
urlpatterns += [
    url(
        r'^events/create/$',
        views.EventCreate.as_view(),
        name='event-create',
    ),
    url(
        r'^events/(?P<pk>\d+)/update/$',
        views.EventUpdate.as_view(),
        name='event-update',
    ),
    url(
        r'^events/(?P<pk>\d+)/delete/$',
        views.EventDelete.as_view(),
        name='event-delete',
    ),
]

# Event partic
urlpatterns += [
    url(
        r'^event/(?P<pk>\d+)/partic/$',
        views.CustomEventViews.do_participate,
        name='i-do-event',
    ),
    url(
        r'^event/(?P<pk>\d+)/not-partic/$',
        views.CustomEventViews.dont_participate,
        name='i-remind-event',
    ),
    url(
        r'^event/missing-space/$',
        views.CustomEventViews.event_missing_space,
        name='missing-space-event',
    ),
    url(
        r'^event/partic/(?P<pk>\d+)/confirm/$',
        views.CustomEventViews.confirm_partic,
        name='partic-confirm',
    ),
]
