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
        views.user_account_view,
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

# User list & detail
urlpatterns += [
    url(
        r'^users/$',
        views.UsersListView.as_view(),
        name='users',
    ),
    url(
        r'^user/(?P<pk>\d+)$',
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

# Users create
urlpatterns += [
    url(
        r'^create-user/$',
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
