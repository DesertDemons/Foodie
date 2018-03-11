from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Restaurant(models.Model):
	name = models.CharField(max_length=25)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()
	established = models.DateField()

	def __str__(self):
		return "Name: [" + self.name + "] " + self.description

	def get_absolute_url(self):
		return reverse("restaurants_menu", kwargs={"Restaurant_id": self.id})
#class PostModelAdmin(admin.ModelAdmin):
	#list_display = ["title", "timestamp", "updated"]
	# list_filter = ["timestamp"]
	# search_fields = ["title", "content"]
	# list_display_links = ['timestamp']
	# class Meta:
	#     model = Post 

class Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=3)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) 

	def __str__(self):
		return "Name: [" + self.name + "] " + self.description

class FavRest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Fav_Item(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
