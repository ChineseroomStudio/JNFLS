from django.contrib import admin

from .models import Broadcast


class BroadcastAdmin(admin.ModelAdmin):
	list_display = ['creator', 'date', 'time']

admin.site.register(Broadcast, BroadcastAdmin)
