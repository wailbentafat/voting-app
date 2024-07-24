from django.contrib import admin
from .models import Candidate, Event, User

admin.site.register(Candidate)

admin.site.register(User)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'expiration_date')
    filter_horizontal = ('candidates',)


