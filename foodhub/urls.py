"""foodhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurants import views 
#rom django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', views.menu, name="restaurants_list"),
    path('main_dish/<int:Restaurant_id>/', views.main_dish, name="restaurants_menu"),
    path('create/', views.create, name="create_rest"),
    path('update/<int:Restaurant_id>/', views.update, name="update_rest"),
    path('delete/<int:Restaurant_id>/', views.delete, name="delete_rest"),
    #url(r'^admin/', admin.site.urls),
]
