from django.contrib import admin
from .models import Event, Participant


# Register your models here.
admin.site.register(Event)
# admin.site.register(Participant)


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('profile', 'event', 'confirm')
    list_filter = ('profile', 'event')
    fieldsets = (
        (None, {
            'fields': ('event', 'confirm')
        }),
        ('Availability', {
            'fields': ('profile',)
        }),
    )
