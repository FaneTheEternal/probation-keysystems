from django.contrib import admin
from .models import Event, Participant


# Register your models here.
admin.site.register(Event)
# admin.site.register(Participant)


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'confirm')
    list_filter = ('user', 'event')
    fieldsets = (
        (None, {
            'fields': ('event', 'confirm')
        }),
        ('Availability', {
            'fields': ('user',)
        }),
    )
