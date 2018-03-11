from django import forms
from .models import Restaurant, Item
from django.contrib.auth.models import User

class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ['name','description','established']
		# we can make shortcut for fields by typing just
		# fields = '__all__'

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = '__all__'


class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
		widgets = {
			"password": forms.PasswordInput()
		}

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())