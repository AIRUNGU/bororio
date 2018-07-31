from django.db import models

class Category(models.Model):
	title = models.CharField(max_length=200)
	price = models.FloatField()
	range_days = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class AdvReports(models.Model):
	title = models.CharField(max_length=200)
	price = models.IntegerField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


	class Meta:
		verbose_name_plural = 'AdvReports'
		ordering = ['-created']

	def __str__(self):
		return self.title

class Safaris(models.Model):
	place = models.CharField(max_length=150)
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	image = models.ImageField(upload_to='Safarimedia/%y/%m/%d', blank=False)
	description = models.TextField()

	def __str__(self):
		return self.place

	class Meta:
		verbose_name_plural = 'Safaris'

