from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm
# Create your views here.
def menu(request):
	context = {
		"restaurants": Restaurant.objects.all(),
	}
	# context = {
	# 	"restaurants": [
	# 	{
	# 	"type": "こんにちは",
	# 	"dishes": " to choose from main dishes...",
	# 	"drinks": "a verity of drinks...",
	# 	"desserts": "Cakes and hearts breaks",
	# 	},
	# 	{
	# 	"type": "Marhaba...",
	# 	"dishes": " to choose from main dishes...",
	# 	"drinks": "a verity of drinks...",
	# 	"desserts": "Cakes and hearts breaks",
	# 	},
	# 	{
	# 	"type": "Howdy...",
	# 	"dishes": " to choose from main dishes...",
	# 	"drinks": "a verity of drinks...",
	# 	"desserts": "Cakes and hearts breaks",
	# 	},
	# 	{
	# 	"type": "Indian...",
	# 	"dishes": " to choose from main dishes...",
	# 	"drinks": "a verity of drinks...",
	# 	"desserts": "Cakes and hearts breaks",
	# 	},		
	# 	]
	# }
	return render(request, 'menu.html', context)

def main_dish(request, Restaurant_id):
	context = {
		"details": Restaurant.objects.get(id=Restaurant_id),
	}
	# context = {
	# 	"title": "This is main dish",
	# 	"Chicken": "Fried Chicken",
	# 	"Steaks": "No more regretting for your mistakes",
	# 	"Fish": "always a choice if you don't know how to pick a dish"
	# }
	return render(request, 'main_dish.html', context)

def create(request):
	form = RestaurantForm()
	if request.method == "POST":
		form = RestaurantForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("restaurants_list")
	context = {
		"form": form,
	}
	return render(request, 'create_rest.html', context)

def update(request, Restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=Restaurant_id)
	form = RestaurantForm(instance=restaurant_obj)
	if request.method == "POST":
		form = RestaurantForm(request.POST, instance=restaurant_obj)
		if form.is_valid():
			form.save()
			return redirect("restaurants_menu", Restaurant_id=restaurant_obj.id)
	context = {
		"form": form,
		"obj": restaurant_obj,
	}
	return render(request, 'update_rest.html', context)

def delete(request, Restaurant_id):
	Restaurant.objects.get(id=Restaurant_id).delete()
	# messages.success(request, "Successfully Deleted!")
	# restaurant_obj = Restaurant.objects.get(id=Restaurant_id)
	# restaurant_obj.delete()

	return redirect("restaurants_list")
	
