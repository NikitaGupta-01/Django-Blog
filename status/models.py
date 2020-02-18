from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Status(models.Model):
	user		=	models.ForeignKey(User,on_delete=models.CASCADE)
	content 	= 	models.TextField(null=True, blank=True)
	updated		=	models.DateTimeField(auto_now=True)
	timestamp	=	models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)[:50]

