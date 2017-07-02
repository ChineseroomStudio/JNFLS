from django.db import models


class Broadcast(models.Model):
	TIME_CHOICE = ((1, '上午跑操'),
	               (2, '中午午休'),
	               (3, '下午跑操'),
	               (4, '晚自习前'))

	content = models.TextField()
	is_approved = models.BooleanField(default=False)

	creator = models.ForeignKey('accounts.Account')
	date = models.DateField()
	time = models.IntegerField(choices=TIME_CHOICE)

	def __str__(self):
		# TODO: bad implementation
		return str(self.date) + ' ' + str(self.time)
