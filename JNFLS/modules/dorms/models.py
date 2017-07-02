from django.db import models


class Dorm(models.Model):
	dorm_number = models.IntegerField(default=0)

	def __str__(self):
		return self.dorm_number
