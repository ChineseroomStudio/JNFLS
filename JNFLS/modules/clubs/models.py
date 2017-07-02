from django.db import models


# 社团
class Club(models.Model):
	name = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
