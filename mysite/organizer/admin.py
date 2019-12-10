from django.contrib import admin
from .models import Event, EventOptions, Participant


# Register your models here.
admin.site.register(Event)
admin.site.register(EventOptions)
admin.site.register(Participant)
