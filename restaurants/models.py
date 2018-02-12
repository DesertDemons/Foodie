from django.db import models
from django.urls import reverse

class Restaurant(models.Model):
	name = models.CharField(max_length=25)
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