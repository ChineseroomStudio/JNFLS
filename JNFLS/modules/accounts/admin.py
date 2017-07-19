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
	readonly_fields = ('created', 'updated', 'is_staff',)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields' : ('username', 'password')}
		 ),
	)

admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
