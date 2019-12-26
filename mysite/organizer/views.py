from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from .models import Participant, Profile

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
        context['is_participate'] = Participant.objects\
            .filter(event=context['event'])\
            .filter(user=self.request.user).count() != 0
        return context


@login_required
def user_account_view(request):
    return render(
        request,
        'organizer/account_detail.html',
    )


class UserEventsListView(LoginRequiredMixin, generic.ListView):
    model = Participant

    template_name = 'organizer/participant_list.html'

    def get_queryset(self):
        return Participant\
            .objects\
            .filter(user=self.request.user)


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = [
        'title',
        'allow_wife',
        'allow_family',
        'for_kids',
        'number_of_participants',
        'event_date',
        'prepay_date',
        'personal_transportation',
        'company_transport',
        'company_transport_size',
        'main_price',
        'other_prices',
        'deposit',
        'some_properties',
    ]

    def form_valid(self, form):
        user = self.request.user
        if not user.profile.is_moderator:
            raise PermissionDenied
        obj = form.save(commit=False)
        obj.owner = user
        obj.save()
        return redirect('event-detail', pk=obj.id, permanent=True)


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = [
        'title',
        'allow_wife',
        'allow_family',
        'for_kids',
        'number_of_participants',
        'event_date',
        'prepay_date',
        'personal_transportation',
        'company_transport',
        'company_transport_size',
        'main_price',
        'other_prices',
        'deposit',
        'some_properties',
    ]

    def form_valid(self, form):
        obj = form.save(commit=False)
        user = self.request.user
        if not user.profile.is_moderator:
            raise PermissionDenied
        obj.save()
        return redirect('event-detail', pk=obj.id, permanent=True)


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events')


class CustomEventViews(LoginRequiredMixin):
    """
    Views for operations on events
    """
    def confirm_partic(request, pk):
        if not request.user.profile.is_moderator:
            raise PermissionDenied
        partic = get_object_or_404(Participant, pk=pk)
        partic.confirm = True
        partic.save()
        return redirect(
            'event-detail',
            pk=partic.event.id,
            permanent=True,
        )

    def not_confirm_partic(request, pk):
        if not request.user.profile.is_moderator:
            raise PermissionDenied
        partic = get_object_or_404(Participant, pk=pk)
        partic.confirm = False
        partic.save()
        return redirect(
            'event-detail',
            pk=partic.event.id,
            permanent=True,
        )

    def event_missing_space(request):
        return render(
            request,
            'organizer/missing_space_event.html',
        )

    def do_participate(request, pk):
        user = request.user
        event = get_object_or_404(Event, pk=pk)
        count_already = event.participant_set.count()
        number_of_participants = event.number_of_participants
        confirm = False
        if event.deposit is None:
            confirm = True

        if number_of_participants and number_of_participants < count_already:
            return redirect('missing-space-event', permanent=True)

        participant = Participant(
            user=user,
            event=event,
            confirm=confirm,
        )

        participant.save()
        return redirect('user-events', permanent=True)

    def dont_participate(request, pk):
        user = request.user
        event = get_object_or_404(Event, pk=pk)

        partic = Participant.objects\
            .filter(user=user)\
            .filter(event=event)[0]
        partic.delete()
        return redirect('user-events', permanent=True)


class UsersListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    paginate_by = 10

    def get_queryset(self):
        return Profile.objects.all().order_by('user__first_name')


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile


class CustomUserViews():
    """
    Custom views for operations on users
    """
    def toggle_moderator_status(request, pk):
        user = get_object_or_404(User, pk=pk)
        user.profile.is_moderator = not user.profile.is_moderator
        user.save()
        return redirect('user-detail', pk=pk)


class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    fields = [
        'username',
        'password',
        'first_name',
        'last_name',
        'email',
    ]

    template_name = 'organizer/user_form.html'

    def form_valid(self, form):
        user = self.request.user
        if not user.is_superuser:
            raise PermissionDenied
        obj = form.save(commit=False)
        obj.save()
        return redirect('user-detail', pk=obj.id, permanent=True)


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = [
        'first_name',
        'last_name',
        'email',
    ]

    template_name = 'organizer/user_form.html'

    def form_valid(self, form):
        user = self.request.user
        if not user.is_superuser:
            raise PermissionDenied
        obj = form.save(commit=False)
        obj.save()
        return redirect('user-detail', pk=obj.id, permanent=True)


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'organizer/user_confirm_delete.html'
    success_url = reverse_lazy('users')
