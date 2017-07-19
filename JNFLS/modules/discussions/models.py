from django.db import models


# 聊天版
class DiscussionBoard(models.Model):
	TYPE_CHOICES = (
		(0, '校园讨论版'),
		(1, '班级讨论版'),
		(2, '社团讨论版')
	)

	name = models.CharField(max_length=100)

	my_class = models.OneToOneField('classes.SchoolClass', related_name='discussion_board', null=True)
	my_club = models.OneToOneField('clubs.Club', related_name='discussion_board', null=True)
	type = models.IntegerField(choices=TYPE_CHOICES)

	def __str__(self):
		return self.name


# 帖子
class DiscussionPost(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()

	board = models.ForeignKey('DiscussionBoard', related_name='posts')
	creator = models.ForeignKey('accounts.Account', related_name='my_discussion_posts')

	is_anonymous = models.BooleanField(default=False)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


# 回帖
class DiscussionReply(models.Model):
	content = models.TextField()

	creator = models.ForeignKey('accounts.Account', related_name='replies')
	post = models.ForeignKey('DiscussionPost', related_name='replies')
	reply_to = models.ForeignKey('DiscussionReply', null=True)

	is_anonymous = models.BooleanField(default=False)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.content
