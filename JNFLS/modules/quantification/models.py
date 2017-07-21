from django.db import models


class Quantification(models.Model):
	number = models.IntegerField()
	reason = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now_add=True)

	person = models.ForeignKey('accounts.Account')
	school_class = models.ForeignKey('classes.SchoolClass')
	dorm = models.ForeignKey('dorms.Dorm')

	class Meta:
		permissions = (
			('can_person', '可以对个人扣分'),
			('can_class', '可以对班级扣分'),
			('can_dorm', '可以对宿舍扣分'),
		)
