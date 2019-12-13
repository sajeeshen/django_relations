from django.contrib import admin
from core.models import Place, Restaurant
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    fields = ('place', 'name', 
            'food_choices')
    list_display = ('place', 'name',
                'food_choices', 
                'created', 'updated', 'get_place_address')
    
    def get_place_address(self, obj):
        return obj.place.address
    get_place_address.short_description = 'Address'
    get_place_address.admin_order_field = 'place.address'


admin.site.register(Place)
admin.site.register(Restaurant, RestaurantAdmin)
