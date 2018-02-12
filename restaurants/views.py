from django.shortcuts import render
from .models import Restaurant

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