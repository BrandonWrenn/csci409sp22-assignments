from django.contrib import admin
from tickets.models import Ticket, Reservation
# Register your models here.


class TicketInline(admin.StackedInline):
    model = Ticket
    extra = 2


class ReservationAdmin(admin.ModelAdmin):
    field = ['flight', 'num_people', 'total_cost']
    inlines = [TicketInline]

admin.site.register(Reservation, ReservationAdmin)
