from django.contrib import admin

from django.contrib import admin

from .models import Cuisine, Food, Order

class CuisineAdmin(admin.ModelAdmin):
    list_display = ('catagory','created_at')
    search_fields = ('catagory',)
    ordering = ('catagory',)
    
    
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','price','is_available')
    search_fields = ('name',)
    list_editable = ('is_available',)
    list_filter = ('is_available',)
    ordering = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display= ('id','user','order_details','is_ready','is_delivered')
    list_editable= ('is_ready','is_delivered')
    ordering = ('-id',)

admin.site.register(Cuisine,CuisineAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(Order,OrderAdmin)
    