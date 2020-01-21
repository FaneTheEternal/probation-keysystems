from . import views
from django.conf.urls import url


urlpatterns = [
    url(
        r'^$',
        views.CustomViews.index,
        name='index'
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
        r'^event/(?P<pk>\d+)/$',
        views.EventDetailView.as_view(),
        name='event-detail',
    ),
]

# Event create & upd & del
urlpatterns += [
    url(
        r'^events/create$',
        views.EventCreate.as_view(),
        name='event-create',
    ),
    url(
        r'^events/(?P<pk>\d+)/update$',
        views.EventUpdate.as_view(),
        name='event-update',
    ),
    url(
        r'^events/(?P<pk>\d+)/delete$',
        views.EventDelete.as_view(),
        name='event-delete',
    ),
]

# Event partic
urlpatterns += [
    url(
        r'^event/(?P<pk>\d+)/missing-space$',
        views.CustomEventViews.event_missing_space,
        name='missing-space-event',
    ),
    url(
        r'^partic/(?P<pk>\d+)/toggle-confirm$',
        views.CustomEventViews.toggle_confirm,
        name='toggle-confirm',
    ),
]
