from django.contrib import admin
from .models import User,Event,Ticket,UserTicket,EventOrganizerProposal
# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(UserTicket)
admin.site.register(EventOrganizerProposal)
