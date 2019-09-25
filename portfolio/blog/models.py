from django.db import models
import datetime

class Blog(models.Model):
	title=models.CharField(max_length=200,default="")
	body=models.TextField(default="")
	image=models.ImageField(upload_to='images/', default=None)
	pub_date=models.DateTimeField(default=None)

	def __str__(self):
		return self.title

	def summary(self):
		return (self.body[:100]+'...')
