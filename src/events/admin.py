from django.contrib import admin
from .models import Event, SubscribeEmail, Order

# Register your models here.

admin.site.register(Event)
admin.site.register(SubscribeEmail)
admin.site.register(Order)