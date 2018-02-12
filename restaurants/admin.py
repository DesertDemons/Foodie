from django.contrib import admin
from .models import Restaurant
#from .models import Post

#class PostModelAdmin(admin.ModelAdmin):
    #class Meta:
        #model = Post

#admin.site.register(Post, PostModelAdmin)
# Register your models here.
admin.site.register(Restaurant)
