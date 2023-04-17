from django.contrib import admin
from event_app.models import Events,Participants
# Register your models here.
# admin.site.register(Events, Participants)

class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'description', 'venue']

class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ['user', 'event_name', 'is_registered']

admin.site.register(Events, EventAdmin)
admin.site.register(Participants, ParticipantsAdmin)