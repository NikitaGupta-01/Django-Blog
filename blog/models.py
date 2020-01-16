from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=100)
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User , on_delete=models.CASCADE ,null=False, blank=False) #one to many relationship where user i.e author is in User table that we import 
												 #on_delete will delete the post if author is deleted not vice versa
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail' , kwargs={'pk': self.pk})
