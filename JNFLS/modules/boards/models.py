from django.db import models


# 聊天版
class DiscussionBoard(models.Model):
	name = models.CharField(max_length=100)

	my_class = models.OneToOneField('classes.SchoolClass', related_name='board', null=True)
	my_club = models.OneToOneField('clubs.Club', related_name='board', null=True)

	def __str__(self):
		return self.name


# 帖子
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()

	board = models.ForeignKey('DiscussionBoard', related_name='posts')
	creator = models.ForeignKey('accounts.Account', related_name='posts')

	is_anonymous = models.BooleanField(default=False)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


# 回帖
class Reply(models.Model):
	content = models.TextField()

	creator = models.ForeignKey('accounts.Account', related_name='replies')
	post = models.ForeignKey('Post', related_name='replies')
	reply_to = models.ForeignKey('Reply', null=True)

	is_anonymous = models.BooleanField(default=False)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.content
