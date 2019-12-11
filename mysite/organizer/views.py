from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User
from .models import Participant

from .models import Event


# Create your views here.
@login_required
def index(request):
    return render(
        request,
        'index.html',
    )


class EventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    paginate_by = 10


class EventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event


class UserDetailView(LoginRequiredMixin, generic.ListView):
    model = User

    template_name = 'organizer/user_detail.html'

    def get_queryset(self):
        return Participant\
            .objects\
            .filter(user=self.request.user)\
            .order_by('event.data')
