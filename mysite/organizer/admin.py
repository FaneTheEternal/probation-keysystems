from django.contrib import admin
from .models import Event, Participant


# Register your models here.
admin.site.register(Event)
# admin.site.register(Participant)


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'confirm', 'some_custom_data')
    list_filter = ('user', 'event')
    fieldsets = (
        (None, {
            'fields': ('event', 'confirm', 'some_custom_data')
        }),
        ('Availability', {
            'fields': ('user',)
        }),
    )
