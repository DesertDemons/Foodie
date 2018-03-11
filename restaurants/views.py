from django.shortcuts import render, redirect
from .models import Restaurant, FavRest, Item
from .forms import RestaurantForm, UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.http import HttpResponse, Http404
# Create your views here.
def menu(request):
	restaurants = Restaurant.objects.all()
	# order objects by name and date of  established
	restaurants = restaurants.order_by('name', 'established')
	query = request.GET.get('q')
	if query:
		restaurants = restaurants.filter(name__contains=query)

	# if user not logged in he can't see the list page
	if request.user.is_anonymous:
		return redirect('login')

	fav_list = []
	favourits = request.user.favrest_set.all()
	for favourit in favourits:
		fav_list.append(favourit.restaurant)

	context = {
		"restaurants": restaurants,
		"fav_list": fav_list,
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
	# item = Item.objects.get(id=item_id)
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
	if not(request.user.is_staff or request.user==restaurant_obj.owner):
	# rais Http404
	# return redirect('page name')
		return HttpResponse("<h1>Error you are not the owner or staff member</h1>")
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
	if not (request.user.is_staff):
		return HttpResponse("<h1>You don't have the permission to delete</h1>")
	Restaurant.objects.get(id=Restaurant_id).delete()
	# messages.success(request, "Successfully Deleted!")
	# restaurant_obj = Restaurant.objects.get(id=Restaurant_id)
	# restaurant_obj.delete()

	return redirect("restaurants_list")
	
def user_register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			# user = form.save(commit=False)
			my_user = user.username
			my_password = user.password
			user.set_password(user.password)
			user.save()
			
			login(request, user)
			return redirect("restaurants_list")
	context = {
		"form": form
	}
	return render(request, 'register.html', context)

def user_login(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			auth_user = authenticate(username=my_username, password=my_password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("restaurants_list")
	context = {
		"form": form
	}
	return render(request, 'login.html', context)

def userlogout(request):
    logout(request)
    return redirect("restaurants_list")

def create_item(request, Restaurant_id):
	form = ItemForm()
	restaurant_obj = Restaurant.objects.get(id=Restaurant_id)
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			item_obj = form.save(commit=False)
			item_obj.restaurant = restaurant_obj
			item_obj.save()
			return redirect("restaurants_list")
	context = {
		"form": form,
		"restaurant": restaurant_obj,
	}
	return render(request, 'create_item.html', context)


def fav(request, Restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=Restaurant_id)
	fav_obj, created = FavRest.objects.get_or_create(user=request.user, restaurant=restaurant_obj)

	if created:
		action="Favourited"
	else:
		action="unfavourited"
		fav_obj.delete()

	fav_count=restaurant_obj.favrest_set.all().count()
	# or we can do it as
	# fav_count = Fav_rest.objects.filter(Restaurant=restaurant_obj)

	context = {
		"action": action,
		"count": fav_count,
	}
	return JsonResponse(context, safe=False)
