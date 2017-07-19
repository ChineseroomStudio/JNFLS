from django.contrib import admin

from .models import SchoolClass


class SchoolClassAdmin(admin.ModelAdmin):
	list_display = ['grade', 'number', 'head_teacher']


admin.site.register(SchoolClass, SchoolClassAdmin)
