from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 255)

	class Meta:
		ordering = ('name',)
		#it shows the categories sorted by acseding order of name

		#functionality of Class Meta
		#verbose_name_plural and other fixed name variables
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name
		#shows the original name of the objects created from
		#model using the user interface. normally it shows
		#like object1, object2..

class Item(models.Model):
	def __str__(self):
		return self.name
		
	category = models.ForeignKey(Category, related_name = 'items', on_delete = models.CASCADE)
	name = models.CharField(max_length = 255)
	description = models.TextField(blank = True, null = True)
	price = models.FloatField()
	image = models.ImageField(upload_to = 'item_images', blank = True, null = True)
	is_sold = models.BooleanField()
	created_by = models.ForeignKey(User, related_name='items', on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
