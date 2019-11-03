from django.db import models

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
	country=models.CharField(max_length=100)
	subject=models.CharField(max_length=500)


	def __str__(self):
		return self.subject