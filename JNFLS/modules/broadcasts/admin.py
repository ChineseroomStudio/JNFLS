from django.contrib import admin

from .models import Broadcast


@admin.register(Broadcast)
class BroadcastAdmin(admin.ModelAdmin):
	list_display = ['creator', 'date', 'time']
