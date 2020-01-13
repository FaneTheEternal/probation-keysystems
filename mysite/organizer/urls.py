from . import views
from django.conf.urls import url


urlpatterns = [
    url(
        r'^$',
        views.CustomViews.index,
        name='index'
    ),
    url(
        r'^account/$',
        views.CustomViews.account_view,
        name='account',
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
        r'^event/missing-space$',
        views.CustomEventViews.event_missing_space,
        name='missing-space-event',
    ),
    url(
        r'^partic/(?P<pk>\d+)/toggle-confirm$',
        views.CustomEventViews.toggle_confirm,
        name='toggle-confirm',
    ),
]

# User list & detail
urlpatterns += [
    url(
        r'^users/$',
        views.UsersListView.as_view(),
        name='users',
    ),
    url(
        r'^user/(?P<pk>\d+)/$',
        views.UserDetailView.as_view(),
        name='user-detail',
    ),
]

# User toggle moderator status
urlpatterns += [
    url(
        r'^user/(?P<pk>\d+)/do-moder$',
        views.CustomUserViews.toggle_moderator_status,
        name='toggle-moderator-status',
    ),
]

# Users create & update & delete
urlpatterns += [
    url(
        r'^create-user$',
        views.UserCreate.as_view(),
        name='user-create',
    ),
    url(
        r'^user/(?P<pk>\d+)/update$',
        views.UserUpdate.as_view(),
        name='user-update',
    ),
    url(
        r'^user/(?P<pk>\d+)/delete$',
        views.UserDelete.as_view(),
        name='user-delete',
    ),
]
