from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_participate"] = Participant.objects.filter(event=context['event']).filter(user=self.request.user).count() != 0
        return context


@login_required
def UserDetailView(request):
    return render(
        request,
        'organizer/user_detail.html',
    )


class UserEventsListView(LoginRequiredMixin, generic.ListView):
    model = Participant

    template_name = 'organizer/participant_list.html'

    def get_queryset(self):
        return Participant\
            .objects\
            .filter(user=self.request.user)


@login_required
def ParticipateView(request, pk):
    user = request.user
    event = get_object_or_404(Event, pk=pk)
    confirm = False
    if event.deposit is None:
        confirm = True

    participant = Participant(
        user=user,
        event=event,
        confirm=confirm,
        some_custom_data='',
    )

    participant.save()
    return reverse_lazy('user-events')


@login_required
def ParticipateDeleteVeiw(request, pk):
    user = request.user
    event = get_object_or_404(Event, pk=pk)

    partic = Participant.objects.filter(user=user).filter(event=event)[0]
    partic.delete()
    return reverse_lazy('user-events')
