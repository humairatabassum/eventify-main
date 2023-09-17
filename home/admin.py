from django.contrib import admin
from home.models import accounts, events, venue, booking, booked, payment

# Register your models here.
admin.site.register(accounts)
admin.site.register(events)
admin.site.register(venue)
admin.site.register(booking)
admin.site.register(booked)
admin.site.register(payment)
