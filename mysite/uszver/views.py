from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from organizer.models import Participant
from .models import Profile

# Create your views here.


class CustomViews(LoginRequiredMixin):
    """
    Some custom general purpose views
    """
    def account_view(request):
        return render(
            request,
            'uszver/account_detail.html',
        )


class UserEventsListView(LoginRequiredMixin, generic.ListView):
    model = Participant

    template_name = 'uszver/participant_list.html'

    def get_queryset(self):
        return Participant\
            .objects\
            .filter(user=self.request.user)\
            .order_by('event')


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

    template_name = 'uszver/user_form.html'

    def form_valid(self, form):
        user = self.request.user
        if not user.is_superuser:
            raise PermissionDenied
        obj = form.save(commit=False)
        obj.save()
        return redirect('user-detail', pk=obj.id, permanent=True)


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'uszver/user_confirm_delete.html'
    success_url = reverse_lazy('users')
