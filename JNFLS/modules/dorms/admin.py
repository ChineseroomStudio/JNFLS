from django.contrib import admin

from .models import Dorm


class DormAdmin(admin.ModelAdmin):
	list_display = ['dorm_number']


admin.site.register(Dorm, DormAdmin)
