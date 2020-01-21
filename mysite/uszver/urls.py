from django.conf.urls import url
from . import views

urlpatterns = [
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
