from django.db import models


# 班级
class SchoolClass(models.Model):
	GRADE_CHOICE = ((1, '高一'),
	                (2, '高二'),
	                (3, '高三'))

	number = models.IntegerField(default=0)
	grade = models.IntegerField(choices=GRADE_CHOICE)
	head_teacher = models.ForeignKey('accounts.Account')
	slogan = models.CharField(max_length=100)


# 流动红旗
class RedFlag(models.Model):
	name = models.CharField(max_length=100)
