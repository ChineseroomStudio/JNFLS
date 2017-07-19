from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import Account
from .forms import AccountChangeForm, AccountCreationForm


class AccountAdmin(UserAdmin):
	form = AccountChangeForm
	add_form = AccountCreationForm

	list_display = ['username', 'created']
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('个人信息', {'fields': ('first_name', 'last_name')}),
		('权限', {'fields': ('is_staff',)}),
		('时间戳', {'fields': ('created', 'updated')})
	)
	readonly_fields = ['created', 'updated']

	add_fieldsets = (
		(None, { 'classes': ('wide',), 'fields' : ('username', 'password', 'type', )}),
		('权限 (选填)', {'fields': ('is_student_union', 'is_head_teacher', 'is_staff', )}),
		('学生信息 (选填)',{'fields': ('my_student_union_dep', 'my_schoolclass', 'my_dorm' )})
	)

admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
