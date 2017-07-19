from django.db import models


# 公告板
class PostBoard(models.Model):
	TYPE_CHOICES = (
		(0, '校园公告版'),
		(1, '班级公告版'),
		(2, '社团公告版')
	)

	name = models.CharField(max_length=100)

	my_class = models.OneToOneField('classes.SchoolClass', related_name='post_board', null=True)
	my_club = models.OneToOneField('clubs.Club', related_name='post_board', null=True)
	type = models.IntegerField(choices=TYPE_CHOICES)

	def __str__(self):
		return self.name


# 公告
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()

	board = models.ForeignKey('PostBoard', related_name='posts')
	creator = models.ForeignKey('accounts.Account', related_name='my_posts')

	is_anonymous = models.BooleanField(default=False)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
