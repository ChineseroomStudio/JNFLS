from django.contrib import admin

from .models import Club


class ClubAdmin(admin.ModelAdmin):
	list_display = ['name', 'club_head']


admin.site.register(Club, ClubAdmin)
