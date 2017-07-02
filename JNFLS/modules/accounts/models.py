from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# 账户管理器
class AccountManager(BaseUserManager):
	use_in_migrations = True

	def _create_account(self, password, **extra_fields):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not extra_fields.get('username'):
			raise ValueError('The username must be set')

		account = self.model(**extra_fields)
		account.set_password(password)
		account.save()
		return account

	def create_user(self, password=None, **extra_fields):
		extra_fields['is_superuser'] = False
		extra_fields['is_staff'] = False
		return self._create_account(password, **extra_fields)

	def create_superuser(self, password, **extra_fields):
		extra_fields['is_superuser'] = True
		extra_fields['is_staff'] = True
		return self._create_account(password, **extra_fields)


# 账户
class Account(AbstractBaseUser, PermissionsMixin):
	TYPE_CHOICES = (
		(0, '学生'),
		(1, '家长'),
		(2, '教师')
	)
	# Auth
	username = models.CharField(max_length=40, unique=True, null=True)
	# Account Info
	alias = models.CharField(max_length=20, null=True)
	avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
	type = models.IntegerField(choices=TYPE_CHOICES, default=0)
	# Required by BaseUser
	first_name = models.CharField(max_length=40, null=True, blank=True)
	last_name = models.CharField(max_length=40, null=True, blank=True)
	# Permission
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	is_student_union = models.BooleanField(default=False)
	is_head_teacher = models.BooleanField(default=False)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# Relations
	objects = AccountManager()
	#
	my_department = models.ForeignKey('StudentUnionDepartment', null=True, blank=True)
	my_schoolclass = models.ForeignKey('classes.SchoolClass', null=True, blank=True)
	my_clubs = models.ManyToManyField('clubs.Club')
	# my_dorm = models.ForeignKey('Dorm', null=True, blank=True)

	# Settings
	USERNAME_FIELD = 'username'

	class Meta:
		ordering = ['created']

	def __str__(self):
		return self.username

	def full_name(self):
		return self.username

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return self.username


class StudentUnionDepartment(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name
