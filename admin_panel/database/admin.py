from django.contrib import admin

from .models import CarModel, NFTCar, User

class NFTCarAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'token_id', 'owned', 'part', 'secret_code', 'model')
    
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id',)
    
admin.site.register(NFTCar, NFTCarAdmin, )
admin.site.register( CarModel, CarModelAdmin,)
admin.site.register(User, UserAdmin)