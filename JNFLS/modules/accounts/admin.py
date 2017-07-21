from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

from .models import Account
from .forms import AccountChangeForm, AccountCreationForm


#
# class UserSetInline(admin.TabularInline):
# 	model = User.groups.through
# 	# raw_id_fields = ('user',)  # optional, if you have too many users
#
#
# admin.site.unregister(Group)
#
#
# @admin.register(Group)
# class MyGroupAdmin(GroupAdmin):
# 	inlines = [UserSetInline]
#

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
		('权限', {'fields': ('is_staff', 'groups')}),
		('时间戳', {'fields': ('created', 'updated')})
	)
	readonly_fields = ['created', 'updated']

	add_fieldsets = (
		(None, {'classes': ('wide',), 'fields': ('username', 'password', 'type',)}),
		('权限 (选填)', {'fields': ('is_student_union', 'is_head_teacher', 'is_staff',)}),
		('学生信息 (选填)', {'fields': ('my_student_union_dep', 'my_schoolclass', 'my_dorm')})
	)
