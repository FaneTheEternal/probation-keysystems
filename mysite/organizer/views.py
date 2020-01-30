from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from .models import Participant, Event
from .forms import EventForm


# Create your views here.
class CustomViews(LoginRequiredMixin):
    """
    Some custom general purpose views
    """
    def index(request):
        if not request.user.is_authenticated:
            return redirect(
                'login',
                permanent=True,
            )
        obj_list = Event.objects.all()
        return render(
            request,
            'index.html',
            {
                'user': request.user,
                'list': obj_list,
            },
        )


class EventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    paginate_by = 10


class EventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = context['event']
        is_participate = Participant.objects\
            .filter(event=event)\
            .filter(user=self.request.user).count() != 0

        context['is_participate'] = is_participate
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = super(EventDetailView, self).get_context_data(**kwargs)
        event = context['event']

        if 'i-do' in request.POST:
            imp = event.number_of_participants == event.participant_set.count()
            imp |= event.is_past()
            if imp:
                return redirect(
                   'missing-space-event',
                   pk=event.id,
                   permanent=True,
                )

            context['is_participate'] = True
            confirm = not event.deposit
            partic = Participant(
                event=event,
                user=self.request.user,
                confirm=confirm,
                )
            partic.save()
        elif 'i-dont' in request.POST:
            context['is_participate'] = False
            partic = Participant.objects\
                .filter(event=event, user=self.request.user)[0]
            partic.delete()

        return self.render_to_response(context=context)


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm

    def form_valid(self, form):
        if not self.request.user.profile.is_moderator:
            raise PermissionDenied
        form.instance.owner = self.request.user
        return super(EventCreate, self).form_valid(form)


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm

    def form_valid(self, form):
        if not self.request.user.profile.is_moderator:
            raise PermissionDenied
        return super(EventUpdate, self).form_valid(form)


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events')


class CustomEventViews(LoginRequiredMixin):
    """
    Views for operations on events
    """
    def event_missing_space(request, pk):
        return render(
            request,
            'organizer/missing_space_event.html',
            {'pk': pk},
        )

    def toggle_confirm(request, pk):
        if not request.user.profile.is_moderator:
            raise PermissionDenied
        partic = get_object_or_404(Participant, pk=pk)
        partic.confirm = not partic.confirm
        partic.save()
        return redirect('event-detail', pk=partic.event.id)
