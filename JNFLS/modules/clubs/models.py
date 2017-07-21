from django.db import models


# 社团
class Club(models.Model):
	name = models.CharField(max_length=100)

	club_head = models.ForeignKey('accounts.Account', related_name='head_clubs')
	club_manager = models.ManyToManyField('accounts.Account', related_name='managing_clubs')
	club_members = models.ManyToManyField('accounts.Account', related_name='my_clubs')

	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		permissions = (
			("club_manager", "可以管理社团"),
			("class_post", "可以发布班级公告"),
			("club_post", "可以发布社团公告"),
		)

	def __str__(self):
		return self.name


# 社团活动
class Event(models.Model):
	title = models.CharField(max_length=100)
	start = models.DateTimeField()
	end = models.DateTimeField()
	club = models.ForeignKey('CLub')

	def __str__(self):
		return self.title
