from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import Event


# Create your views here.
@login_required
def index(request):
    return render(
        request,
        'index.html',
    )


class EventListView(generic.ListView):
    model = Event
    paginate_by = 10


class EventDetailView(generic.DetailView):
    model = Event
