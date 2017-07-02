from django.db import models


# 聊天版
class DiscussionBoard(models.Model):
	name = models.CharField(max_length=100)

	my_class = models.OneToOneField('classes.SchoolClass', related_name='board', null=True)
	my_club = models.OneToOneField('clubs.Club', related_name='board', null=True)

	def __str__(self):
		return self.name
