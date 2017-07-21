from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import Account
from .forms import AccountChangeForm, AccountCreationForm


@admin.register(Account)
class AccountAdmin(UserAdmin):
	def group(self, user):
		groups = []
		for group in user.groups.all():
			groups.append(group.name)
		return ' '.join(groups)

	group.short_description = 'Groups'

	form = AccountChangeForm
	add_form = AccountCreationForm

	list_display = ['username', 'created', 'group']
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('个人信息', {'fields': ('first_name', 'last_name')}),
		('权限', {'fields': ('is_staff',)}),
		('时间戳', {'fields': ('created', 'updated')})
	)
	readonly_fields = ['created', 'updated']

	add_fieldsets = (
		(None, {'classes': ('wide',), 'fields': ('username', 'password', 'type',)}),
		('权限 (选填)', {'fields': ('is_student_union', 'is_head_teacher', 'is_staff',)}),
		('学生信息 (选填)', {'fields': ('my_student_union_dep', 'my_schoolclass', 'my_dorm')})
	)
