from django.db import models
from django.utils import timezone


# 公告板
class PostBoard(models.Model):
	TYPE_CHOICES = (
		(0, '校园公告版'),
		(1, '班级公告版'),
		(2, '社团公告版')
	)

	name = models.CharField(max_length=100)

	my_class = models.OneToOneField('classes.SchoolClass', related_name='post_board', null=True, blank=True)
	my_club = models.OneToOneField('clubs.Club', related_name='post_board', null=True, blank=True)
	type = models.IntegerField(choices=TYPE_CHOICES)

	def __str__(self):
		return self.name


# 公告
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()

	board = models.ForeignKey('PostBoard', related_name='posts', on_delete=models.CASCADE)
	creator = models.ForeignKey('accounts.Account', related_name='my_posts')

	views = models.IntegerField(default=0)

	created = models.DateTimeField(editable=False)
	updated = models.DateTimeField()

	class Meta:
		permissions = (
			("school_post", "可以发布校园公告"),
			("class_post", "可以发布班级公告"),
			("club_post", "可以发布社团公告"),
		)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		""" On save, update timestamps """
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Post, self).save(*args, **kwargs)
